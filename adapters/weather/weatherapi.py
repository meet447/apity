import requests

def make_request(city: str, api_key: str) -> dict:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"q": city, "key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def normalize(data: dict) -> dict:
    return {
        "location": data["location"]["name"],
        "temperature_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }