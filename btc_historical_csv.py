import csv
import os
import json
from datetime import datetime

import pandas as pd
from binance.client import Client

test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

client = Client(test_api_key, test_api_secret)

# valid intervals - 1m, 3m, 1h, 12h, 1d, 1M
timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1m')
date = datetime.utcfromtimestamp(timestamp/1000)
print(date)

bars = client.get_historical_klines('BTCUSDT', '1d', timestamp, limit=1000)
# print(bars)

# delete redundant data - keep date, open, high, low, close
for line in bars:
    del line[5:]

# bars into Pandas DF and export to csv
btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
btc_df['date'] = pd.to_datetime(btc_df['date'], unit='ms')
btc_df.set_index('date', inplace=True)
print(btc_df.tail())

btc_df.to_csv('btc_bars3.csv')