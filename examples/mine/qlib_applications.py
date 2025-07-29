import sys
import os
import multiprocessing

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def main():
    import qlib
    from qlib.data import D
    from qlib.config import REG_CN
    from qlib.workflow import R
    from qlib.utils import init_instance_by_config
    import pandas as pd
    import numpy as np

    # 初始化Qlib
    qlib.init(provider_uri="d:/stockdata/.qlib/qlib_data/cn_data", region=REG_CN)
    
    print("=" * 60)
    print("Qlib主要应用场景展示")
    print("=" * 60)
    
    # 1. 数据获取和处理
    print("1. 数据获取和处理")
    print("-" * 30)
    # 获取沪深300成分股
    instruments = D.instruments('csi300')
    print(f"沪深300成分股数量: {len(list(instruments))}")
    
    # 获取多因子数据
    features = ['$close', '$open', '$high', '$low', '$volume', '$change']
    df = D.features(D.instruments('csi300'), features, start_time='2020-01-01', end_time='2020-01-10')
    print(f"获取因子数据形状: {df.shape}")
    print("因子列表:", features)
    print()
    
    # 2. 因子分析
    print("2. 因子分析")
    print("-" * 30)
    # 计算简单移动平均因子
    close_prices = df.loc[:, '$close']
    # 获取单只股票数据进行演示
    first_stock = df.index.get_level_values('instrument').unique()[0]
    stock_data = df.loc[first_stock, '$close']
    sma_5 = stock_data.rolling(window=5).mean()
    print(f"计算{first_stock}的5日移动平均线:")
    print(sma_5.tail())
    print()
    
    # 3. 策略构建
    print("3. 策略构建")
    print("-" * 30)
    # 简单的移动平均交叉策略示例
    print("构建简单的移动平均交叉策略:")
    print("- 当短期均线(5日)上穿长期均线(10日)时买入")
    print("- 当短期均线下穿长期均线(10日)时卖出")
    print()
    
    # 4. 模型训练准备
    print("4. 模型训练准备")
    print("-" * 30)
    # 构造机器学习特征和标签
    # 以5日后收益率作为标签
    feature_df = df.loc[:, features]
    print("特征数据形状:", feature_df.shape)
    print("可用于机器学习模型训练")
    print()
    
    # 5. 回测框架
    print("5. 回测框架")
    print("-" * 30)
    print("Qlib提供完整的回测框架，支持:")
    print("- 交易成本模拟")
    print("- 滑点模拟")
    print("- 不同交易策略评估")
    print("- 绩效指标计算")
    print()
    
    # 6. 风险管理
    print("6. 风险管理")
    print("-" * 30)
    print("支持的风险管理功能:")
    print("- 投资组合优化")
    print("- 风险因子分析")
    print("- 最大回撤控制")
    print("- 仓位管理")
    print()
    
    # 7. 模型集成
    print("7. 模型集成")
    print("-" * 30)
    print("Qlib支持多种机器学习模型:")
    print("- 线性模型 (Linear)")
    print("- 树模型 (LightGBM, XGBoost)")
    print("- 深度学习模型 (LSTM, GRU, Transformer)")
    print("- 强化学习模型")
    print()
    
    print("=" * 60)
    print("这些只是Qlib功能的一部分，更多功能请参考官方文档和examples目录")
    print("=" * 60)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()