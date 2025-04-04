from fastapi import FastAPI
import requests

app = FastAPI()

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

@app.get("/price")
def get_price(symbol: str = "bitcoin", currency: str = "usd"):
    endpoint = f"{COINGECKO_API_URL}/simple/price"
    params = {
        "ids": symbol.lower(),
        "vs_currencies": currency.lower()
    }

    response = requests.get(endpoint, params=params)

    if response.status_code != 200:
        return {
            "error": f"CoinGecko API error: {response.status_code}",
            "details": response.text
        }

    try:
        data = response.json()
    except Exception as e:
        return {
            "error": "Failed to parse response",
            "message": str(e)
        }

    if symbol.lower() not in data:
        return {
            "error": "Symbol not found",
            "requested_symbol": symbol
        }

    return {
        "symbol": symbol.lower(),
        "currency": currency.lower(),
        "price": data[symbol.lower()][currency.lower()]
    }