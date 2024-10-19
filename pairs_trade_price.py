import os
from time import sleep

import pandas as pd
from binance import ThreadedWebsocketManager
from binance.client import Client

api_key = os.environ.get('binance_test_api')
api_secret = os.environ.get('binance_test_secret')

client = Client(api_key, api_secret, testnet=True)

price = {'BTCUSDT': None, 'error':False}

def btc_pairs_trade(msg):
    if msg['e'] != 'error':
        price['BTCUSDT'] = float(msg['c'])
    else:
        price['error'] = True
