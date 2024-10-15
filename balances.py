import os

from binance.client import Client

# credentials
test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

client = Client(test_api_key, test_api_secret)

client.API_URL = 'https://testnet.binance.vision/api'

