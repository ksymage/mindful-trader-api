
from fastapi import FastAPI
import requests

app = FastAPI()

BINANCE_API_URL = "https://api.binance.com/api/v3"

@app.get("/price")
def get_price(symbol: str = "BTCUSDT", interval: str = "1h", limit: int = 1):
    endpoint = f"{BINANCE_API_URL}/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    response = requests.get(endpoint, params=params)
    data = response.json()[0]

    return {
        "symbol": symbol,
        "open_time": data[0],
        "open": data[1],
        "high": data[2],
        "low": data[3],
        "close": data[4],
        "volume": data[5]
    }
