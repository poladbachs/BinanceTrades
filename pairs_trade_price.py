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


bsm = ThreadedWebsocketManager()
bsm.start()
bsm.start_symbol_ticker_socket(
    symbol='BTCUSDT',
    callback=btc_pairs_trade)

while not price['BTCUSDT']:
    sleep(0.1)

print(client.get_asset_balance(asset='USDT'))

while True:
    if price['error']:
        bsm.stop()
        sleep(2)
        bsm.start()
        price['error'] = False

    else:
        if price['BTCUSDT'] > 68000:
            try:
                order = client.order_market_buy(symbol='ETHUSDT', quantity=0.1)
                print(f"BUY ETH IF BTC HITS 68,000: {order}")
                break
            except Exception as e:
                print(e)

    sleep(0.1)

bnb_price = client.get_symbol_ticker(symbol='ETHUSDT')
print(client.get_asset_balance(asset='ETH'))
print(client.get_asset_balance(asset='USDT'))

bsm.stop()