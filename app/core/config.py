from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME:str 
    APP_VERSION:str 
    DEBUG_MODE:bool 
    DEFAULT_DOWNLOAD_CHUNK_MB:int 
    TEST_SERVER_IP:str
    IP_API_URL:str 

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore",   
    )

settings = Settings()   

    