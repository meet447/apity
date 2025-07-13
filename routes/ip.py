from fastapi import APIRouter, Query, HTTPException
from models.ip import IPGeoResponse
from services.selector import select_ip_provider
from plugins.ip import post_response

router = APIRouter()

@router.get("/ip-geolocation", response_model=IPGeoResponse)
def get_ip_data(ip: str = Query(...)):
    provider = select_ip_provider()

    try:
        raw = provider["module"].make_request(ip, provider["key"])
        normalized = provider["module"].normalize(raw)
        return post_response(normalized)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))