import os
from typing import Dict

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    UPLOAD_DIRECTORY: str = os.getenv("UPLOAD_DIRECTORY")
    AWS_S3_ENDPOINT: str = os.getenv("AWS_S3_ENDPOINT")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION_NAME: str = os.getenv("AWS_REGION_NAME")
    # AWS_CONFIG: Dict[str,str] = {
    #     "ENDPOINT_URL": "http://localstack:4566",
    #     "AWS_ACCESS_KEY_ID": "test",
    #     "AWS_SECRET_ACCESS_KEY": "test",
    #     "REGION_NAME": "us-east-1",
    # }
    model_config = ConfigDict(env_file=".env")


settings = Settings()
