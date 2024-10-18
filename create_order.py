import os

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

test_api_key = os.environ.get('binance_api')
test_api_secret = os.environ.get('binance_secret')

client = Client(test_api_key, test_api_secret)
    
buy_order_limit = client.create_test_order(
	symbol='ETHUSDT',
	side='BUY',
	type='LIMIT',
	timeInForce='GTC',
	quantity=1,
	price=2000)

buy_order = client.create_test_order(symbol='ETHUSDT', side='BUY', type='MARKET', quantity=1)

exchange_info = client.get_exchange_info()
for symbol in exchange_info['symbols']:
    if symbol['symbol'] == 'ETHUSDT':
        print(symbol['filters'])

symbol_ticker = client.get_symbol_ticker(symbol="ETHUSDT")
current_price = float(symbol_ticker['price'])

price = round(current_price * 0.99, 2)
print(f"Placing a limit order at: {price}")