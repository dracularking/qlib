import sys
import os
import multiprocessing

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def main():
    import qlib
    from qlib.data import D
    from qlib.config import REG_CN

    # 初始化Qlib
    qlib.init(provider_uri="d:/stockdata/.qlib/qlib_data/cn_data", region=REG_CN)
    
    print("=" * 50)
    print("Qlib数据结构解释")
    print("=" * 50)
    
    # 获取沪深300指数成分股
    instruments = D.instruments('csi300')
    print(f"1. 沪深300指数成分股示例:")
    print(instruments)
    print()
    
    # 加载部分数据进行展示
    print("2. 加载少量沪深300指数成分股的收盘价数据:")
    # 使用时间限制来减少数据量
    df = D.features(D.instruments('csi300'), ['$close'], start_time='2020-01-01', end_time='2020-01-10')
    print("数据形状:", df.shape)
    print("索引名称:", df.index.names)
    print("列名:", list(df.columns))
    print()
    
    # 显示数据
    print("3. 实际数据展示:")
    print(df)
    print()
    
    # 解释MultiIndex结构
    print("4. MultiIndex结构解释:")
    print("   - instrument: 股票代码 (如 SH600000)")
    print("   - datetime:   交易日期 (如 2005-01-04)")
    print("   - $close:     标准化后的收盘价")
    print()
    
    # 展示如何访问特定股票数据
    print("5. 访问特定股票数据的方法:")
    if len(df) > 0:
        instrument_list = df.index.get_level_values('instrument').unique()
        if len(instrument_list) > 0:
            first_instrument = instrument_list[0]
            print(f"   选择第一只股票: {first_instrument}")
            instrument_data = df.loc[first_instrument]
            print("   该股票的数据:")
            print(instrument_data)
    print()
    
    # 解释数据值的含义
    print("6. 关于数据值的说明:")
    print("   Qlib中的价格数据是经过标准化处理的，不是原始价格")
    print("   这样处理是为了让数据更适合机器学习模型训练")
    print("   如果需要原始价格，需要进行反向转换或使用原始数据源")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()