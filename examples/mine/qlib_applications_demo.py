import sys
import os
import multiprocessing

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def main():
    import qlib
    from qlib.data import D
    from qlib.config import REG_CN
    import pandas as pd
    import numpy as np

    # 初始化Qlib
    qlib.init(provider_uri="d:/stockdata/.qlib/qlib_data/cn_data", region=REG_CN)
    
    print("=" * 60)
    print("Qlib主要应用场景展示")
    print("=" * 60)
    
    # 1. 数据获取和处理
    print("\n1. 数据获取和处理")
    print("-" * 40)
    # 获取沪深300成分股
    instruments = D.instruments('csi300')
    print(f"沪深300成分股: {instruments}")
    
    # 获取多因子数据
    features = ['$close', '$open', '$high', '$low', '$volume', '$change']
    df = D.features(D.instruments('csi300'), features, start_time='2020-01-01', end_time='2020-01-31')
    print(f"获取因子数据形状: {df.shape}")
    print("因子列表:", features)
    print()
    
    # 2. 因子分析
    print("2. 因子分析示例")
    print("-" * 40)
    # 计算简单移动平均因子
    close_prices = df.loc[:, '$close'].dropna()
    print("部分股票收盘价数据:")
    print(close_prices.head(10))
    
    # 选择一只股票计算移动平均
    sample_stock = close_prices.index.get_level_values('instrument')[0]
    stock_close = df.loc[sample_stock, '$close']
    print(f"\n{sample_stock} 的收盘价:")
    print(stock_close.head())
    
    # 计算移动平均线
    sma_5 = stock_close.rolling(window=5).mean()
    print(f"\n{sample_stock} 的5日移动平均线:")
    print(sma_5.head(10))
    print()
    
    # 3. 策略构建概念
    print("3. 策略构建概念")
    print("-" * 40)
    print("Qlib支持构建多种量化投资策略:")
    print("  - 技术指标策略 (如移动平均线交叉)")
    print("  - 多因子选股策略")
    print("  - 机器学习驱动策略")
    print("  - 深度学习策略")
    print("  - 强化学习交易策略")
    print()
    
    # 4. 机器学习准备
    print("4. 机器学习数据准备")
    print("-" * 40)
    # 构造特征和标签
    feature_data = df.loc[:, ['$open', '$high', '$low', '$close', '$volume']]
    print("特征数据形状:", feature_data.shape)
    
    # 构造简单的标签 (未来5日收益率)
    # 这里只是示意，实际应用中需要更复杂的处理
    print("可用于构建机器学习模型的数据集")
    print("特征包括: 开盘价、最高价、最低价、收盘价、成交量")
    print("标签可以是: 未来收益率、涨跌分类等")
    print()
    
    # 5. 回测框架
    print("5. 回测框架")
    print("-" * 40)
    print("Qlib提供完整的回测功能:")
    print("  - 支持交易成本和滑点模拟")
    print("  - 多样化的绩效评估指标")
    print("  - 风险分析和归因分析")
    print("  - 投资组合优化")
    print()
    
    # 6. 支持的模型
    print("6. 支持的机器学习模型")
    print("-" * 40)
    print("Qlib内置多种机器学习模型:")
    print("  - 传统模型: 线性回归、岭回归")
    print("  - 树模型: XGBoost、LightGBM、CatBoost")
    print("  - 神经网络: LSTM、GRU、Transformer")
    print("  - 强化学习: PPO、DDPG等")
    print()
    
    # 7. 实际应用案例
    print("7. 实际应用案例")
    print("-" * 40)
    print("使用Qlib可以实现:")
    print("  - 量化因子研究")
    print("  - 策略回测和优化")
    print("  - 风险模型构建")
    print("  - 投资组合管理")
    print("  - 交易执行优化")
    print("  - 高频交易策略")
    print()
    
    print("=" * 60)
    print("这些展示了Qlib的主要功能和应用场景")
    print("更多详细示例请参考examples目录中的完整代码")
    print("=" * 60)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()