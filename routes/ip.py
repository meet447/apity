from fastapi import APIRouter, Query, HTTPException
from models.ip import IPGeoResponse
from services.selector import IP_PROVIDERS  # <- import full list, not selector
from plugins.ip import post_response

router = APIRouter()

@router.get("/ip-geolocation", response_model=IPGeoResponse)
def get_ip_data(ip: str = Query(...)):
    last_error = None

    for provider in IP_PROVIDERS:
        try:
            raw = provider["module"].make_request(ip, provider["key"])
            normalized = provider["module"].normalize(raw)
            return post_response(normalized)
        except Exception as e:
            last_error = e
            continue

    # All providers failed
    raise HTTPException(status_code=502, detail=f"All IP providers failed: {str(last_error)}")