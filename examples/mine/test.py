import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import qlib
from qlib.data import D

print(f"Qlib file location: {qlib.__file__}")
print(f"Qlib version: {qlib.__version__}")
print(f"Qlib has init: {hasattr(qlib, 'init')}")

# 初始化Qlib，指定数据路径
qlib.init(provider_uri="d:/stockdata/.qlib/qlib_data/cn_data")

# 现在您可以使用Qlib加载数据了
# 例如，加载沪深300指数的股票数据
df = D.features(D.instruments('csi300'), ['CLOSE'])
print(df.head())