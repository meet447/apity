from fastapi import APIRouter, Query, HTTPException
from models.search import SearchResponse
from services.selector import select_search_provider
from plugins.search import post_response

router = APIRouter()

@router.get("/search", response_model=SearchResponse)
def search_route(q: str = Query(...)):
    provider = select_search_provider()

    try:
        raw = provider["module"].make_request(q, provider["key"])
        normalized = provider["module"].normalize(raw)
        return post_response(normalized)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))