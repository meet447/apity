import random
from adapters.weather import openweather, weatherapi
from config import WEATHERAPI_KEY, OPENWEATHER_KEY

PROVIDERS = [
    {
        "name": "weatherapi",
        "module": weatherapi,
        "key": WEATHERAPI_KEY
    },
    {
        "name": "openweather",
        "module": openweather,
        "key": OPENWEATHER_KEY
    }
]

def select_weather_provider():
    return random.choice(PROVIDERS)  # or round-robin, failover, etc.