import json
import urllib.request
from fastapi import Request
from app.core.config import settings
import httpx

#data generator
def dummy_data_generator(size_in_mb: int):
    chunk_1mb = b"\x00" * (1024 * 1024)
    for _ in range(size_in_mb):
        yield chunk_1mb

# Get client IP (resolving localhost/local dev environment and proxy headers)
def get_client_ip(request: Request) -> str:
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    if x_forwarded_for:
        client_host = x_forwarded_for.split(",")[0].strip()
    else:
        client_host = request.client.host if request.client else None

    if not client_host or client_host in ["127.0.0.1", "localhost", "::1"]:
        return settings.TEST_SERVER_IP
    return client_host

#Network detector
async def detect_network_info(client_ip: str) -> dict:
    try:
        url = settings.IP_API_URL + "json/" + client_ip + "?fields=status,message,query,country,city,regionName,lat,lon,isp,org,as"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=3.0)

            if response.status_code == 200:
                data = response.json()
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

