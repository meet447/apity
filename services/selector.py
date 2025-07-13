import random
from adapters.weather import openweather, weatherapi
from config import WEATHERAPI_KEY, OPENWEATHER_KEY
from adapters.ip import ipapi, ipinfo
from adapters.search import duckduckgo
from adapters.search import google

SEARCH_PROVIDERS = [
    {
        "name": "duckduckgo",
        "module": duckduckgo,
        "key": "your_serpapi_key"
    },
    {
        "name": "google",
        "module": google,
        "key": "your_google_key"
    }
]

def select_search_provider():
    from random import choice
    return choice(SEARCH_PROVIDERS)
    
IP_PROVIDERS = [
    {
        "name": "ipapi",
        "module": ipapi,
        "key": "your_ipapi_key"  # optional (free tier works without)
    },
    {
        "name": "ipinfo",
        "module": ipinfo,
        "key": "your_ipinfo_key"
    }
]

def select_ip_provider():
    from random import choice
    return choice(IP_PROVIDERS)
    
    
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