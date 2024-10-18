import pandas as pd

btc_df = pd.read_csv('btc_bars3.csv', index_col=0)
btc_df.index = pd.to_datetime(btc_df.index)

btc_df['20sma'] = btc_df.close.rolling(20).mean()
print(btc_df.tail(5))

mean = btc_df.close.tail(20).mean()

max_btc_value = btc_df.loc['2024']['close'].max()

print(mean)
print(max_btc_value)