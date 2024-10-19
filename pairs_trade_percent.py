import os
from time import sleep

import pandas as pd
from binance import ThreadedWebsocketManager
from binance.client import Client

futures_test_api_key = os.environ.get('binance_futures_test_api')
futures_test_api_secret = os.environ.get('binance_futures_test_secret')
client = Client(futures_test_api_key, futures_test_api_secret, testnet=True)
price = {'BTCUSDT': pd.DataFrame(columns=['date', 'price']), 'error':False}