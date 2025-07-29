import numpy as np
from qlib.data import D
from qlib import init
from qlib.config import REG_CN
from qlib.utils import exists_qlib_data


def loadInstruments():
    # Initialize Qlib with default data if needed
    if not exists_qlib_data("~/.qlib/qlib_data/cn_data"):
        print("Qlib data not found. Please run 'python scripts/get_data.py' to download data.")
        return
    
    # Initialize Qlib
    init(provider_uri="~/.qlib/qlib_data/cn_data", region=REG_CN)
    
    print("=" * 50)
    print("Loading CSI300 instruments...")
    
    # Load instruments for CSI300
    instruments = D.instruments(market='csi300')
    print(f"Instruments: {instruments}")
    
    # List instruments in the given time range
    instrument_list = D.list_instruments(
        instruments=instruments, 
        start_time='2010-01-01', 
        end_time='2017-12-31', 
        as_list=True
    )
    
    print(f"\nTotal number of instruments: {len(instrument_list)}")
    print(f"First 6 instruments: {instrument_list[:6]}")
    
    # Return the result for potential further use
    return instrument_list[:6]


if __name__ == "__main__":
    result = loadInstruments()
    if result:
        print(f"\nReturned result: {result}")