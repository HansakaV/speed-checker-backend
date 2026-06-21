import json
import urllib.request
from app.core.config import settings

#data generator
def dummy_data_generator(size_in_mb: int):
    chunk_1mb = b"\x00" * (1024 * 1024)
    for _ in range(size_in_mb):
        yield chunk_1mb

#Network detector
def detect_network_info(client_ip: str) -> dict:
    if client_ip in ["127.0.0.1", "localhost", "::1"]:
        client_ip = settings.TEST_SERVER_URL   

    try:
        url = settings.IP_API_URL + "json/" + client_ip + "?fields=status,message,query,country,city,lat,lon,isp,org,as"
        req = urllib.request.Request(url,headers={"User-Agent": "Mozilla/5.0"})

        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode("utf-8"))
            
            if data.get("status") == "success":
                return{
                    "ip":data.get("query", client_ip),
                    "isp":data.get("isp","Unknown"),
                    "location":f"{data.get('city','Unknown')},{data.get('regionName','Unknown')}, {data.get('country','Unknown')}",
                }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    return {
        "ip": client_ip,
        "isp": "Unknown",
        "location": "Unknown"
    }

