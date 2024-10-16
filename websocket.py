from time import sleep

from binance import ThreadedWebsocketManager

btc_price = {'error': False}
eth_price = {'error': False}

def btc_trade_history(msg):
    """Define how to process incoming WebSocket messages"""
    if msg['e'] != 'error':
        print('BTC:',msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
        btc_price['error'] = False
    else:
        btc_price['error'] = True

def eth_trade_history(msg):
    if msg['e'] != 'error':
        print('ETH:',msg['c'])
        eth_price['last'] = msg['c']
        eth_price['bid'] = msg['b']
        eth_price['last'] = msg['a']
        eth_price['error'] = False
    else:
        eth_price['error'] = True

# init and start WebSocket
bsm = ThreadedWebsocketManager(testnet=True)
bsm.start()

bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')

bsm.start_symbol_ticker_socket(callback=eth_trade_history, symbol='ETHUSDT')

while True:
    sleep(2)

bsm.stop()