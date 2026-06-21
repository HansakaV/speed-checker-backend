import os
from fastapi import APIRouter,status,Request
from fastapi.response import StreamingResponse
from app.core.config import settings
from app.features.SpeedCheck import utils

router = APIRouter(
    prefix="/speed-test",
    tags=["Speed-Test-Analysis"]
)

#download Speed Test Endpoint
router.get("/download",status_code=status.HTTP_200_OK)  
async def download_speed_test(size_in_mb: int = settings.DEFAULT_DOWNLOAD_CHUNK_MB):
    return StreamingResponse(
        utils.dummy_data_generator(size_in_mb),
        media_type="application/octet-stream"
    )   

#upload Speed Test Endpoint
router.post("/upload",status_code=status.HTTP_200_OK)
async def upload_speed_test(request:Request):
    body_bytes = 0
    async for chunk in request.stream():
        body_bytes += len(chunk)
          
