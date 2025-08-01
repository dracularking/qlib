from qlib.data.dataset.loader import QlibDataLoader
from qlib.config import REG_CN
from qlib import init

def main():
    init(provider_uri="~/.qlib/qlib_data/cn_data", region=REG_CN)

    # 定义 MACD 表达式（文档 1.17.2）
    MACD_EXP = "(EMA($close, 12) - EMA($close, 26))/$close - EMA((EMA($close, 12) - EMA($close, 26))/$close, 9)/$close"
    fields = [MACD_EXP]
    names = ["MACD"]

    # 加载 CSI300 的 MACD 数据
    data_loader = QlibDataLoader(config={"feature": (fields, names)})
    df = data_loader.load(instruments="csi300", start_time="2010-01-01", end_time="2017-12-31")
    print(df.head())

if __name__ == "__main__":
    main()