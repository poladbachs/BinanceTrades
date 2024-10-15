import os

from binance.client import Client

# spot testnet credentials
test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

# futures testnet credentials
futures_test_api_key = os.environ.get('binance_futures_test_api')
futures_test_api_secret = os.environ.get('binance_futures_test_secret')

client = Client(test_api_key, test_api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

futures_client = Client(futures_test_api_key, futures_test_api_secret)
futures_client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

print(client.get_asset_balance(asset='BTC'))

print(futures_client.futures_account_balance())
