from qlib.data import D
from qlib import init
import os

if __name__ == '__main__':
 
    # Disable multiprocessing for data loading to avoid issues
    os.environ['QLIB_NUM_WORKERS'] = '0'
    
    init(provider_uri="~/.qlib/qlib_data/cn_data")

    # Get data for a stock that exists in the dataset
    data = D.features(
        ["SH603259"], 
        fields=["$open", "$high", "$low", "$close", "$volume"],
        start_time="2020-07-21", 
        end_time="2020-08-01",
        freq="day"
    )

    print("Data for SH603259 from 2020-07-21 to 2020-08-01:")
    print(data.head(10))
    print(f"\nData shape: {data.shape}")