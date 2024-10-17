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

# option 3 - save as CSV file without library, only showing date, open, high, low, close
with ('btc_bars2.csv', 'w') as d:
    for line in bars:
        d.write(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}\n')

# delete redundant data - keep date, open, high, low, close
for line in bars:
    del line[5:]