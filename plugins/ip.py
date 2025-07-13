from ipaddress import ip_address

def post_response(data: dict) -> dict:
    try:
        ip = ip_address(data["ip"])
        data["is_private"] = ip.is_private
    except Exception:
        data["is_private"] = False
    return data