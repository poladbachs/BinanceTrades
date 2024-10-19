import os

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

client = Client(test_api_key, test_api_secret, testnet=True)

symbol = 'ETHUSDT'
quantity = 0.1

ticker = client.get_symbol_ticker(symbol=symbol)
eth_price = float(ticker['price'])

print(f"Current ETH price: {eth_price}")

try:
	order = client.create_oco_order(
		symbol=symbol,
		side='SELL',
		quantity=quantity,
		price=2650,
		stopPrice=2640,
		stopLimitPrice=2640,
		stopLimitTimeInForce='GTC')

except BinanceAPIException as e:
	print(e)
except BinanceOrderException as e:
	print(e)