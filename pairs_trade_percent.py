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

print(client.futures_account_balance())

while True:
    if price['error']:
        bsm.stop()
        sleep(2)
        bsm.start()
        price['error'] = False
    else:
        df = price['BTCUSDT']
        start_time = df.date.iloc[-1] - pd.Timedelta(minutes=5)
        df = df.loc[df.date >= start_time] # fitler DF to contain data of last 5 min
        max_price = df.price.max()
        min_price = df.price.min()

        if df.price.iloc[-1] < max_price * 0.999:
            try:
                order = client.futures_create_order(symbol='ETHUSDT', side="SELL", type="MARKET", quantity="0.3")
                print(f"SELL ETH IF BTC FALLS BY >5%: {order}")
                sleep(300) # Sleep to prevent placing multiple orders too quickly
            except Exception as e:
                print(e)
        elif df.price.iloc[-1] > min_price * 1.001:
            try:
                order = client.futures_create_order(symbol='ETHUDST', side="SELL", type="MARKET", quantity="0.3")
                print(f"BUY ETH IF BTC RISES BY >5%: {order}")
                sleep(300) # Sleep for 5 minutes after placing an order
            except Exception as e:
                print(e)

        sleep(0.1)


print(f"BTC Max Price in 5 min: {max_price}")
print(f"BTC Min Price in 5 min: {min_price}")

eth_price = client.get_symbol_ticker(symbol='ETHUSDT')
print(client.futures_account_balance())

bsm.stop()