# 安装依赖
cd qlib
python setup.py install


# 下载A股数据
python scripts/get_data.py qlib_data --target_dir d:/stockdata/.qlib/qlib_data/cn_data --region cn

# 更新数据
python scripts/data_collector/yahoo/collector.py update_data_to_bin --qlib_data_1d_dir ~/.qlib/qlib_data/cn_data --trading_date 2025-01-01 --end_date 2025-08-02

# Checking the health of the data
python scripts/check_data_health.py check_data --qlib_dir ~/.qlib/qlib_data/cn_data

# 运行预测 + 回测完整流程
cd examples
python run_all_model.py run --models=lightgbm --data_dir=d:/stockdata/.qlib/qlib_data/cn_data

qrun benchmarks/LightGBM/workflow_config_lightgbm_Alpha158_csi500.yaml 