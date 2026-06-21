from pydantic import BaseModel, Field

class UploadSpeedResponse(BaseModel):
    status:str = Field(...,example="Success",description="Status of the upload")
    message:str = Field(...,example="Data Payload Received Successfully",description="Message of the upload")
    bytes_received:float = Field(...,example=0,description="Size of the uploaded data in bytes")

class PingResponse(BaseModel):
    status:str = Field(...,example="pong",description="Status of the ping")
