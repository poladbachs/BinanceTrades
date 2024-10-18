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

# buy_order = client.order_market_buy(symbol=symbol, quantity=quantity)

# print(f"Buy market order done: {buy_order}")

sell_order = client.order_market_sell(symbol=symbol, quantity=quantity)

print(f"Sell market order done: {sell_order}")

print(client.get_asset_balance(asset='ETH'))

print(client.get_asset_balance(asset='USDT'))