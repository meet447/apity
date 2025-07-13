from ddgs import DDGS

def make_request(query: str, key: str = "") -> list:
    results = DDGS().text(query, max_results=10)
    return results

def normalize(data: dict) -> dict:
    results = []
    for result in data:
        results.append({
            "title": result["title"],
            "url": result["href"],
            "snippet": result["body"]
        })
    return {
        "query": "duckduckgo",
        "results": results
    }