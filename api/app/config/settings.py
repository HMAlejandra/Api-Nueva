"""
Application configuration
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Database
    database_url: str

    # Gemini API
    gemini_endpoint: str
    gemini_api_key: str

    # Server
    host: str = "0.0.0.0"
    port: int = 8080

    # Database pool settings
    db_pool_size: int = 5
    db_max_overflow: int = 10
    db_pool_timeout: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

