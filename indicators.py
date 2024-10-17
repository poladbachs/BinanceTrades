import btalib
import pandas as pd

btc_df = pd.read_csv('btc_bars3.csv', index_col=0)
btc_df.index = pd.to_datetime(btc_df.index, unit="ms")

