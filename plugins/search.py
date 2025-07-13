def post_response(data: dict) -> dict:
    # Remove duplicate URLs
    seen = set()
    filtered = []
    for item in data["results"]:
        if item["url"] not in seen:
            seen.add(item["url"])
            filtered.append(item)
    data["results"] = filtered
    return data