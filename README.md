### Binance Futures Trading Bot (Testnet)
# A simple Python CLI bot to place orders on Binance Futures Testnet.

## Setup

# 1.Install dependencies:

pip install -r requirements.txt

# 2.Get your API keys from testnet.binancefuture.com and add them to Bot/client.py:

pythonAPI_KEY    = "your_api_key"
API_SECRET = "your_api_secret"

## How to Run
python cli.py
It will show an interactive menu — just follow the prompts to place an order.
# Example:
Symbol     : BTCUSDT
Side       : BUY
Order Type : MARKET
Quantity   : 0.01
For a LIMIT order, you'll also be asked for a price.

## Assumptions

-Uses Binance Futures Testnet only — no real money involved
-LIMIT orders use timeInForce=GTC by default
-On the testnet, MARKET orders sometimes show avgPrice: 0.00 — this is normal, the testnet doesn't always fill orders instantly
-Supported symbols: BTCUSDT, ETHUSDT, BNBUSDT (more can be added in validators.py)