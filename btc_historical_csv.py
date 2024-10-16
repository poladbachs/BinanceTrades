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
timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
date = datetime.utcfromtimestamp(timestamp/1000)
print(date)

bars = client.get_historical_klines