import requests

def make_request(ip: str, key: str = "") -> dict:
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def normalize(data: dict) -> dict:
    return {
        "ip": data["query"],
        "city": data["city"],
        "region": data["regionName"],
        "country": data["country"],
        "latitude": data["lat"],
        "longitude": data["lon"]
    }