from fastapi import FastAPI
import requests

app = FastAPI()

BINANCE_API_URL = "https://api.binance.com/api/v3"

@app.get("/price")
def get_price(symbol: str = "BTCUSDT", interval: str = "1h", limit: int = 1):
    endpoint = f"{BINANCE_API_URL}/klines"
    params = {
        "symbol": symbol.upper(),
        "interval": interval,
        "limit": limit
    }
    response = requests.get(endpoint, params=params)

    if response.status_code != 200:
        return {
            "error": f"Binance API error: {response.status_code}",
            "details": response.text
        }

    try:
        data = response.json()[0]
    except Exception as e:
        return {
            "error": "Failed to parse response",
            "message": str(e)
        }

    return {
        "symbol": symbol.upper(),
        "open_time": data[0],
        "open": data[1],
        "high": data[2],
        "low": data[3],
        "close": data[4],
        "volume": data[5]
    }