import sys
import os
import multiprocessing

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def main():
    import qlib
    from qlib.data import D
    from qlib.config import REG_CN

    print(f"Qlib file location: {qlib.__file__}")
    print(f"Qlib version: {qlib.__version__}")
    print(f"Qlib has init: {hasattr(qlib, 'init')}")

    # 初始化Qlib，指定数据路径
    qlib.init(provider_uri="d:/stockdata/.qlib/qlib_data/cn_data", region=REG_CN)

    # 现在您可以使用Qlib加载数据了
    # 例如，加载沪深300指数的股票数据
    # 使用$close而不是CLOSE，这是Qlib中的标准命名
    df = D.features(D.instruments('csi300'), ['$close'])
    print(df.head())

if __name__ == '__main__':
    # Windows上需要添加这行来支持多进程
    multiprocessing.freeze_support()
    main()