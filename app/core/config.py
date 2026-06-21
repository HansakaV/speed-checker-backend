from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME:str = "Check-My-Speed-Engine"
    APP_VERSION:str = "1.0.0"
    DEBUG_MODE:bool = True
    DEFAULT_DOWNLOAD_CHUNK_MB:int = 10

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore",   
    )
    
settings = Settings()   

    