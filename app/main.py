import sys
import asyncio

#windows specific 
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print(" Forced Selector Event Loop Policy globally for Speed Test Engine!")

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.features.SpeedCheck.router import router as speed_router

app = FastAPI(
    title="Speed Test Engine",
    description="Speed Test Engine",
    version="1.0.0",
    openapi_url="/openapi.json"
)

#Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(speed_router)

@app.get("/",status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Welcome to the Speed Test Engine"}  

