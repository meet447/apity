import requests
from services.llm_normalizer import llm_normalize

def make_request(city: str, api_key: str) -> dict:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"q": city, "key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def normalize(data: dict) -> dict:
    try:
        return {
            "location": data["location"]["name"],
            "temperature_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }
    except Exception:
        return llm_normalize(task="weather",provider_response=data)