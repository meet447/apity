import requests

def make_request(ip: str, key: str = "") -> dict:
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def normalize(data: dict) -> dict:
    lat, lon = map(float, data["loc"].split(","))
    return {
        "ip": data["ip"],
        "city": data.get("city", ""),
        "region": data.get("region", ""),
        "country": data.get("country", ""),
        "latitude": lat,
        "longitude": lon
    }