import requests
from config import WEATHER_API, CRYPTO_API

def get_weather(lat=17.3850, lon=78.4867):
    try:
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
        res = requests.get(WEATHER_API, params=params)
        data = res.json()

        return {
            "temperature": data["current_weather"]["temperature"],
            "windspeed": data["current_weather"]["windspeed"]
        }
    except:
        return {"error": "Weather API failed"}

def get_crypto():
    try:
        params = {
            "ids": "bitcoin,ethereum",
            "vs_currencies": "usd"
        }
        res = requests.get(CRYPTO_API, params=params)
        data = res.json()

        return {
            "bitcoin_usd": data["bitcoin"]["usd"],
            "ethereum_usd": data["ethereum"]["usd"]
        }
    except:
        return {"error": "Crypto API failed"}