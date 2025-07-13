import requests
from services.llm_normalizer import llm_normalize

def make_request(city: str, api_key: str) -> dict:
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def normalize(data: dict) -> dict:
    try:
        return {
            "location": data["name"],
            "temperature_c": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
    except Exception:
        return llm_normalize(task="weather",provider_response=data)
