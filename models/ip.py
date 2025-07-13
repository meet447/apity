from pydantic import BaseModel

class IPGeoResponse(BaseModel):
    ip: str
    city: str
    region: str
    country: str
    latitude: float
    longitude: float