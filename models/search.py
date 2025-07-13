from pydantic import BaseModel
from typing import List

class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]