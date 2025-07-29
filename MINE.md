# 安装依赖
cd qlib
python setup.py install


# 下载A股数据
python scripts/get_data.py qlib_data --target_dir d:/stockdata/.qlib/qlib_data/cn_data --region cn

# 运行预测 + 回测完整流程
cd examples
python run_all_model.py run --models=lightgbm --data_dir=d:/stockdata/.qlib/qlib_data/cn_data




 qrun benchmarks/LightGBM/workflow_config_lightgbm_Alpha158_csi500.yaml 