import os

from binance.client import Client

test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

client = Client(test_api_key, test_api_secret)

btc_price = client.get_symbol_ticker(symbol='BTCUSDT')

print(btc_price)