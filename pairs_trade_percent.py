import os
from time import sleep

import pandas as pd
from binance import ThreadedWebsocketManager
from binance.client import Client

futures_test_api_key = os.environ.get('binance_futures_test_api')
futures_test_api_secret = os.environ.get('binance_futures_test_secret')
client = Client(futures_test_api_key, futures_test_api_secret, testnet=True)

price = {'BTCUSDT': pd.DataFrame(columns=['date', 'price']), 'error':False}

def btc_pairs_trade(msg):
    if msg['e'] != 'error':
        price['BTCUSDT'].loc[len(price['BTCUSDT'])] = [pd.Timestamp.now(), float(msg['c'])]

bsm = ThreadedWebsocketManager()
bsm.start()
bsm.start_symbol_ticker_socket(
    symbol='BTCUSDT', 
    callback=btc_pairs_trade)

while len(price['BTCUSDT']) == 0:
    sleep(1)

sleep(300)

while True:
    if price['error']:
        bsm.stop()
        sleep(2)
        bsm.start()
        price['error'] = False