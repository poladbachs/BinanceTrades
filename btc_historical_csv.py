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

bars = client.get_historical_klines('BTCUSDT', '1m', timestamp, limit=1)
# print(bars)

# option 1 - save to file using json - list of lists
with open('btc_bars.json', 'w') as e:
    json.dump(bars, e)

# option 2 - save as CSV file using the csv writer library
with open('btc_bars.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    for line in bars:
        wr.writerow(line)