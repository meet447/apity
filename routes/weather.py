from fastapi import APIRouter, Query, HTTPException
from models.weather import WeatherResponse
from services.selector import select_weather_provider
from plugins.weather import post_response

router = APIRouter()

@router.get("/weather", response_model=WeatherResponse)
def get_weather(city: str = Query(...)):
    provider = select_weather_provider()

    try:
        raw_response = provider["module"].make_request(city, provider["key"])
        normalized = provider["module"].normalize(raw_response)
        final_output = post_response(normalized)
        return final_output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))