from googlesearch import search

def make_request(query: str, key: str = "") -> list:
    results = list(search(query, num_results=10, unique=True, advanced=True))
    return results

def normalize(data: dict) -> dict:
    results = []
    for result in data:
        results.append({
            "title": result.title,
            "url": result.url,
            "snippet": result.description
        })
    return {
        "query": "googlesearch",
        "results": results
    }