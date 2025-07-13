from fastapi import APIRouter, Query, HTTPException
from models.weather import WeatherResponse
from services.selector import WEATHER_PROVIDERS  # import full provider list
from plugins.weather import post_response

router = APIRouter()

@router.get("/weather", response_model=WeatherResponse)
def get_weather(city: str = Query(...)):
    last_error = None

    for provider in WEATHER_PROVIDERS:
        try:
            raw_response = provider["module"].make_request(city, provider["key"])
            normalized = provider["module"].normalize(raw_response)
            return post_response(normalized)
        except Exception as e:
            last_error = e
            continue

    raise HTTPException(status_code=502, detail=f"All weather providers failed: {str(last_error)}")