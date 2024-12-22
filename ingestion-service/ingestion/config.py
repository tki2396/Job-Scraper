from functools import lru_cache
import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Optional LinkedIn credentials for scraping profile
    LINKEDIN_USERNAME: str | None = os.environ.get('LINKEDIN_USERNAME')
    LINKEDIN_PASSWORD: str | None = os.environ.get('LINKEDIN_PASSWORD')

@lru_cache
def get_settings():
    return Settings()
