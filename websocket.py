from time import sleep

from binance import ThreadedWebsocketManager

btc_price = {'error': False}

def btc_trade_history(msg):
    """Define how to process incoming WebSocket messages"""
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
        btc_price['error'] = False
    else:
        btc_price['error'] = True

# init and start WebSocket
bsm = ThreadedWebsocketManager()
bsm.start()

