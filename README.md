![binance_monkey](https://github.com/user-attachments/assets/b992cb8c-bfe5-4191-a47f-6b3c0ecca0b4)
![ezgif-6-647ec88029](https://github.com/user-attachments/assets/f34cae91-215e-4d1a-b9c2-4c2b65f79316)
# BinanceTrades
Crypto Trading with Binance API

## Project Overview
The Binance Trades project is designed to test and execute various trading actions using the Binance API Spot and Futures testnets. It includes scripts for fetching account balances, retrieving historical data, calculating technical indicators, placing market and limit orders, and implementing pairs trading strategies based on price discrepancies.

## Technologies Used
- **Python Binance** for scripting
- **Binance API** for interacting with Spot and Futures testnets
- **Pandas** for data manipulation
- **Websockets** for real-time price updates
- **OS module** for Binance API Key and Secret variable management

## What I Did in This Project
In the Binance Trades project, I implemented the following scripts:

### `Balances.py`
- Fetched account and asset balances from Binance's Spot and Futures testnets.

### `Latest_BTC_Price.py`
- Retrieved the current BTC price from Binance's testnet.

### `Websocket.py`
- Received real-time price updates for BTC and ETH using WebSocket.

### `BTC_Historical_CSV.py`
- Downloaded historical BTC, ETH, and BNB price data, wrangled each into a Pandas DataFrame, and stored them in separate CSV files.

### `Indicators.py`
- Computed and printed technical indicators such as the 20-day SMA and identified the maximum BTC price in 2024.

### `Create_Order.py`
- Implemented market buy/sell orders, limit orders, and order cancellation for ETH.

### `Stop_Loss_Order.py`
- Created OCO (One Cancels the Other) orders for ETH, setting stop-loss and take-profit prices.

### `Buy_BNB.py`
- Automated the process of topping up BNB to pay for trading fees when its balance falls below a specified threshold.

### `Pairs_Trade_Price.py`
- Executed a market buy order for ETH if the BTC price crosses a defined threshold using WebSocket.

### `Pairs_Trade_Percent.py`
- Executed futures trades on ETH based on BTC price movements, buying ETH when BTC rises significantly and selling ETH when BTC falls dramatically within a 5-minute window, using real-time price updates streamed into a Pandas DataFrame.

## Conclusion
This project provides a comprehensive suite of scripts to interact with the Binance testnets, covering balance checks, historical data retrieval, order placement, and real-time trading strategies.
