
from modules.utils import *
import requests

class Asset:
    def __init__(
            self,
            name,
            ticker,
            isin,
            icon_path,
            symbol,
            data_provider
    ):
        self.name = name
        self.ticker = ticker
        self.isin = isin
        self.icon_path = icon_path
        self.symbol = symbol
        self.data_provider = data_provider
        self.price = "-"
        self.price_delta = "-"
        self.price_delta_percentage = "-"
        self.market_status = "-"

    #update asset price
    def update_asset_price(self):
        price, price_delta, price_delta_percentage, market_status = "-", "-", "-", "-"
        if self.data_provider == "binance":
            price, price_delta, price_delta_percentage, market_status = get_price_update_from_binance(self.symbol)
        elif self.data_provider == "yfinance":
            price, price_delta, price_delta_percentage, market_status = get_price_from_yfinance(self.symbol)

        self.price = price
        self.price_delta = price_delta
        self.price_delta_percentage = price_delta_percentage
        self.market_status = market_status



        #price_update = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={self.symbol}")
        #price_update = price_update.json()
        #self.price = round(float(price_update["lastPrice"]), 2)
        #price_delta = str(round(float(price_update["priceChangePercent"]), 2))
        #price_delta = f"+{price_delta}%" if not price_delta.startswith("-") else f"{price_delta}%"
        #self.price_delta = price_delta
        #price_delta_percentage = str(round(float(price_update["priceChange"]), 2))
        #price_delta_percentage = f"+{price_delta_percentage}" if not price_delta_percentage.startswith("-") else price_delta_percentage
        #self.price_delta_percentage = price_delta_percentage
