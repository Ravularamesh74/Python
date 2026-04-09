from services import get_weather, get_crypto

def aggregate_data():
    weather = get_weather()
    crypto = get_crypto()

    report = {
        "weather": weather,
        "crypto": crypto
    }

    return report