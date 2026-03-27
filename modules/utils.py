
import requests

def get_price_update_from_binance(symbol):
    price_update = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}")
    price_update = price_update.json()
    price = str(round(float(price_update["lastPrice"]), 2)) +"€"
    price_delta = str(round(float(price_update["priceChangePercent"]), 2))
    price_delta = f"+{price_delta}%" if not price_delta.startswith("-") else f"{price_delta}%"
    price_delta_percentage = str(round(float(price_update["priceChange"]), 2))
    price_delta_percentage = f"+{price_delta_percentage}€" if not price_delta_percentage.startswith("-") else price_delta_percentage+"€"
    market_status = "Market open"
    return price, price_delta, price_delta_percentage, market_status


def get_price_from_yfinance(symbol):
    headers = {'User-Agent': 'Mozilla/5.0'}
    price_update = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}", headers=headers)
    price_update = price_update.json()['chart']['result'][0]['meta']
    current_market_price = price_update["regularMarketPrice"]
    previous_close_price = price_update["previousClose"]
    abs_change = current_market_price - previous_close_price
    perc_change = (abs_change / previous_close_price) * 100
    price = round(float(current_market_price), 2)
    price_delta = str(round(float(perc_change), 2))
    price_delta = f"+{price_delta}%" if not price_delta.startswith("-") else f"{price_delta}%"
    price_delta_percentage = str(round(float(abs_change), 2))
    price_delta_percentage = f"+{price_delta_percentage}" if not price_delta_percentage.startswith("-") else price_delta_percentage
    market_status = "Open in 50h 22m"
    return price, price_delta, price_delta_percentage, market_status











#from datetime import datetime, timezone
#def get_market_status(ticker):
    #url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    #headers = {'User-Agent': 'Mozilla/5.0'}
    #response = requests.get(url, headers=headers)
    #meta = response.json()['chart']['result'][0]['meta']
    #state = meta.get("marketState")  # Es: "REGULAR" (Aperto), "CLOSED" (Chiuso)
    #periods = meta.get("currentTradingPeriod", {}).get("regular", {})
    #start_ts = periods.get("start")
    #end_ts = periods.get("end")
    #now_ts = int(datetime.now(timezone.utc).timestamp())
    #status_text = ""
    #countdown = ""
    #if state == "REGULAR":
    #    status_text = "APERTO"
    #    diff = end_ts - now_ts
    #    countdown = f"Chiude tra: {diff // 3600}h {(diff % 3600) // 60}m"
    #else:
    #    status_text = "CHIUSO"
    #    if start_ts > now_ts:
    #        diff = start_ts - now_ts
    #        countdown = f"Apre tra: {diff // 3600}h {(diff % 3600) // 60}m"
    #    else:
    #        countdown = "Apre domani"
    #return {"status": status_text, "timer": countdown, "state": state}