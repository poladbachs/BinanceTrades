import os

from binance.client import Client

test_api_key = os.environ.get('binance_test_api')
test_api_secret = os.environ.get('binance_test_secret')

client = Client(test_api_key, test_api_secret, testnet=True)

bnb_price = client.get_symbol_ticker(symbol='BNBUSDT')

print(bnb_price)

def topup_bnb(min_balance: float, topup: float):
    ''' Topup BNB if it drops below min balance'''
    bnb_balance = client.get_asset_balance('BNB')
    bnb_balance = float(bnb_balance['free'])
    if bnb_balance < min_balance:
        quantity = round(topup - bnb_balance, 5)
        print(quantity)
        order = client.order_market_buy(symbol='BNBUSDT', quantity=quantity)
        return order
    return False


min_balance = 1.5
topup = 1.6
order = topup_bnb(min_balance, topup)
print(f"BNB topup done: {order}")
print(client.get_asset_balance('BNB'))
print(client.get_asset_balance('USDT'))