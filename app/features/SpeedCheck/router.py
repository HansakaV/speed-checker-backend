import os
from fastapi import APIRouter,status,Request
from fastapi.responses import StreamingResponse
from app.core.config import settings
from app.features.SpeedCheck import utils,schems

router = APIRouter(
    prefix="/speed-test",
    tags=["Speed-Test-Analysis"]
)

#download Speed Test Endpoint
@router.get("/download", status_code=status.HTTP_200_OK)  
async def download_speed_test(size_in_mb: int = settings.DEFAULT_DOWNLOAD_CHUNK_MB):
    return StreamingResponse(
        utils.dummy_data_generator(size_in_mb),
        media_type="application/octet-stream"
    )

#upload Speed Test Endpoint
@router.post("/upload",response_model=schems.UploadSpeedResponse,status_code=status.HTTP_200_OK)
async def upload_speed_test(request:Request):
    body_bytes = 0
    async for chunk in request.stream():
        body_bytes += len(chunk)
    
    return schems.UploadSpeedResponse(
        status="Success",
        message="Data Payload Received Successfully",
        bytes_received=body_bytes/1024/1024
    )
    
#ping/latency Speed Test Endpoint
@router.get("/ping",response_model=schems.PingResponse,status_code=status.HTTP_200_OK)
async def ping_speed_test():
    return schems.PingResponse(
        status="pong"
    )   
          
