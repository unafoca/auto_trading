from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

import datetime
import os

# Your keys here
APCA_API_KEY_ID = os.environ['APCA_API_KEY_ID']
APCA_API_SECRET_KEY = os.environ['APCA_API_SECRET_KEY']
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'  # Use the paper trading URL for testing

# Initialize the API
trading_client = TradingClient(APCA_API_KEY_ID, APCA_API_SECRET_KEY, paper=True)


market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=0.0001,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )
