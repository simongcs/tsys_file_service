
import io

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.core.config import settings
from app.services.s3_client import S3Client

router = APIRouter()

s3_client = S3Client(
    endpoint_url=settings.AWS_S3_ENDPOINT,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION_NAME,
)

class S3UploadRequest(BaseModel):
    bucket_name: str
    object_name: str


@router.post("/upload", status_code=201)
async def upload_file(object_name: str, bucket_name: str, file: UploadFile = File(...) ):
    
    try:
        if not s3_client.bucket_exists(bucket_name):
            raise HTTPException(status_code=404, detail="Bucket does not exist.")
        content = await file.read()
        s3_client.upload_file(bucket_name, object_name, content)
        return {"message": "File uploaded successfully."}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/download/")
async def download_file(object_name: str, bucket_name: str):
    try:
        if not s3_client.bucket_exists(bucket_name):
            raise HTTPException(status_code=404, detail="Bucket does not exist.")
        file_content = s3_client.download_file(bucket_name, object_name)
        return StreamingResponse(io.BytesIO(file_content), media_type="application/octet-stream")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    