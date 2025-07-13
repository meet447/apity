def post_response(res: dict) -> dict:
    # Add "is_hot" tag based on temp
    res["is_hot"] = res["temperature_c"] > 30
    return res
    
    