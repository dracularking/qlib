import sys
import os
import multiprocessing

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def main():
    import qlib
    from qlib.data import D
    from qlib.config import REG_CN
    from qlib.strategy import BaseStrategy
    from qlib.backtest import backtest, executor
    from qlib.contrib.evaluate import risk_analysis
    import pandas as pd
    import numpy as np

    # 初始化Qlib
    qlib.init(provider_uri="d:/stockdata/.qlib/qlib_data/cn_data", region=REG_CN)
    
    print("=" * 60)
    print("Qlib简单策略回测示例")
    print("=" * 60)
    
    # 1. 构建简单因子 (价格动量因子)
    print("1. 构建简单因子 (价格动量因子)")
    print("-" * 40)
    
    # 获取沪深300成分股数据
    instruments = D.instruments('csi300')
    
    # 计算20日价格动量因子 (当前价格/20日前价格)
    start_time = '2020-01-01'
    end_time = '2020-12-31'
    
    # 获取收盘价数据
    close_data = D.features(instruments, ['$close'], start_time=start_time, end_time=end_time)
    
    # 计算动量因子
    momentum_period = 20
    momentum_factor = close_data.groupby(level='instrument').apply(
        lambda x: x / x.shift(momentum_period) - 1
    )
    momentum_factor.columns = ['momentum']
    
    print(f"动量因子数据形状: {momentum_factor.shape}")
    print("动量因子示例 (前5行):")
    print(momentum_factor.head())
    print()
    
    # 2. 构建简单策略
    print("2. 构建简单策略")
    print("-" * 40)
    print("策略逻辑:")
    print("- 每个交易日，选择动量因子最高的前10只股票")
    print("- 等权投资这10只股票")
    print("- 每日调仓")
    print()
    
    # 3. 准备回测配置
    print("3. 准备回测配置")
    print("-" * 40)
    
    # 策略配置
    strategy_config = {
        'topk': 10,           # 持仓股票数量
        'n_drop': 0,          # 卖出股票数量
    }
    
    # 回测配置
    backtest_config = {
        'start_time': start_time,
        'end_time': end_time,
        'account': 10000000,  # 初始资金 1000万
        'benchmark': 'SH000300',  # 基准指数 沪深300
        'exchange_kwargs': {
            'limit_threshold': 0.095,     # 涨跌停限制
            'deal_price': 'close',        # 成交价格
            'open_cost': 0.0005,          # 开仓成本
            'close_cost': 0.0015,         # 平仓成本
            'min_cost': 5,                # 最小手续费
        }
    }
    
    print("回测配置:")
    print(f"- 回测时间: {start_time} 到 {end_time}")
    print(f"- 初始资金: 1000万")
    print(f"- 基准指数: 沪深300")
    print(f"- 持仓股票数量: {strategy_config['topk']}")
    print()
    
    # 4. 创建策略类
    print("4. 创建策略类")
    print("-" * 40)
    
    class SimpleMomentumStrategy(BaseStrategy):
        def __init__(self, instruments, momentum_factor, topk, n_drop):
            self.instruments = instruments
            self.momentum_factor = momentum_factor
            self.topk = topk
            self.n_drop = n_drop
            
        def get_signal(self, portfolio, date):
            # 获取当前日期的动量因子值
            current_factors = self.momentum_factor.loc[date].sort_values(by='momentum', ascending=False)
            # 选择动量最高的股票
            buy_candidates = current_factors.index.tolist()
            # 返回买入候选股票和等权权重
            return {stock: 1.0/self.topk for stock in buy_candidates[:self.topk]}
    
    print("策略类创建完成\n")
    
    # 5. 执行回测
    print("5. 执行回测")
    print("-" * 40)
    
    # 创建策略实例
    strategy = SimpleMomentumStrategy(instruments, momentum_factor, strategy_config['topk'], strategy_config['n_drop'])
    
    # 运行回测
    executor_obj = executor.SimulatorExecutor()
    portfolio = backtest(simulator=executor_obj, 
                         strategy=strategy, 
                         **backtest_config)
    
    print("回测执行完成\n")
    
    # 6. 结果分析
    print("6. 结果分析")
    print("-" * 40)
    
    # 计算绩效指标
    risk_df = risk_analysis(portfolio.returns)
    print("绩效指标:")
    print(risk_df)
    
    # 显示投资组合价值变化
    print("\n投资组合价值变化:")
    print(portfolio.returns)
    
    print("\n交易记录:")
    print(portfolio.transactions)
    
    # 5. 结果分析
    print("5. 结果分析")
    print("-" * 40)
    print("Qlib支持的绩效指标:")
    print("- 累计收益率")
    print("- 年化收益率")
    print("- 最大回撤")
    print("- 夏普比率")
    print("- 信息比率")
    print("- 换手率")
    print()
    
    print("=" * 60)
    print("这是一个简化的示例，完整回测需要更多配置")
    print("请参考examples目录中的完整示例")
    print("=" * 60)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()