import os

from binance.client import Client

test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

client = Client(test_api_key, test_api_secret, testnet=True)

btc_price = client.get_symbol_ticker(symbol='BNBUSDT')

print(client.get_asset_balance('BNB'))

min_balance = 0.1
topup = 0.3

def topup_bnb(min_balance: float, topup: float):
    ''' Topup BNB if it drops below min balance'''
