from fastapi import FastAPI

from app.api.file_service import router as file_router

app = FastAPI()

app.include_router(file_router, prefix="/files", tags=["File Service"])
