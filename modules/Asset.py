
import requests

class Asset:
    def __init__(
            self,
            name,
            ticker,
            isin,
            icon_path
    ):
        self.name = name
        self.ticker = ticker
        self.isin = isin
        self.icon_path = icon_path
        self.price = "-"
        self.price_delta = "-"
        self.price_delta_percentage = "-"


    def update_asset_price(self):
        price_update = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCEUR")
        price_update = price_update.json()
        self.price = price_update["lastPrice"]
        self.price_delta = price_update["priceChange"]
        self.price_delta_percentage = price_update["priceChangePercent"]



