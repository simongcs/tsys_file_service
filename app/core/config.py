import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    UPLOAD_DIRECTORY: str = os.getenv("UPLOAD_DIRECTORY")


settings = Settings()