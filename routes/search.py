from fastapi import APIRouter, Query, HTTPException
from models.search import SearchResponse
from services.selector import SEARCH_PROVIDERS  # import the list, not the random selector
from plugins.search import post_response

router = APIRouter()

@router.get("/search", response_model=SearchResponse)
def search_route(q: str = Query(...)):
    last_error = None

    for provider in SEARCH_PROVIDERS:
        try:
            raw = provider["module"].make_request(q, provider["key"])
            normalized = provider["module"].normalize(raw)
            return post_response(normalized)
        except Exception as e:
            last_error = e
            continue

    raise HTTPException(status_code=502, detail=f"All search providers failed: {str(last_error)}")