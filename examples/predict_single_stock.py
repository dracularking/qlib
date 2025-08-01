import pandas as pd
import numpy as np
import qlib
from qlib.config import REG_CN
from qlib.contrib.data.handler import Alpha158
from qlib.data.dataset import DatasetH
from qlib.contrib.model.gbdt import LGBModel
from qlib.workflow import R
from qlib.workflow.record_temp import SignalRecord, SigAnaRecord, PortAnaRecord

# 初始化Qlib
qlib.init(provider_uri="~/.qlib/qlib_data/cn_data", region=REG_CN)

# 定义单只股票
stock_code = "3690.HK"

# 创建数据处理配置
data_handler_config = {
    "start_time": "2018-01-01",
    "end_time": "2023-12-31",
    "fit_start_time": "2018-01-01",
    "fit_end_time": "2021-12-31",
    "instruments": [stock_code],  # 指定单只股票
}

# 创建数据集
dataset = DatasetH(
    handler={
        "class": "Alpha158",
        "module_path": "qlib.contrib.data.handler",
        "kwargs": data_handler_config,
    },
    segments={
        "train": ("2018-01-01", "2021-12-31"),
        "valid": ("2022-01-01", "2022-12-31"),
        "test": ("2023-01-01", "2023-12-31"),
    },
)

# 创建模型
model = LGBModel(
    loss="mse",
    colsample_bytree=0.8879,
    learning_rate=0.2,
    subsample=0.8789,
    lambda_l1=205.6999,
    lambda_l2=580.9768,
    max_depth=8,
    num_leaves=210,
    num_threads=20
)

# 训练模型
print("Training model...")
model.fit(dataset)

# 预测
print("Generating predictions...")
pred = model.predict(dataset, segment="test")

print(f"Predictions for {stock_code}:")
print(pred.head(10))

# 如果需要保存结果
pred.to_csv(f"{stock_code}_predictions.csv")
print(f"Predictions saved to {stock_code}_predictions.csv")