import btalib
import pandas as pd

btc_df = pd.read_csv('btc_bars3.csv', index_col=0)

btc_df['20sma'] = btc_df.close.rolling(20).mean()
print(btc_df.tail(5))