
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app
# from app.api.file_service import router
from app.services.s3_client import S3Client

# app = FastAPI()
# app.include_router(router)
client = TestClient(app)


def get_mock_s3_client():
    mock_s3 = MagicMock(S3Client)
    mock_s3.bucket_exists.return_value = True
    mock_s3.upload_file.return_value = None
    mock_s3.download_file.return_value = b"mock file content"
    return mock_s3

@pytest.fixture()
def mock_s3():
    with patch("app.api.file_service.s3_client", new_callable=get_mock_s3_client) as s3_client:
        yield s3_client


def test_upload_file(mock_s3):
    response = client.post(
        "/files/upload",
        params={"object_name": "test.txt", "bucket_name": "test-bucket"},
        files={"file": ("filename", b"file content")}
    )
    assert response.status_code == 201
    assert response.json() == {"message": "File uploaded successfully."}
    mock_s3.upload_file.assert_called_once_with("test-bucket", "test.txt", b"file content")

def test_upload_file_bucket_not_exists(mock_s3):
    mock_s3.bucket_exists.return_value = False
    response = client.post(
        "/files/upload",
        params={"object_name": "test.txt", "bucket_name": "test-bucket"},
        files={"file": ("filename", b"file content")}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Bucket does not exist."}
    mock_s3.upload_file.assert_not_called()

def test_download_file(mock_s3):
    response = client.post(
        "/files/download/",
        params={"object_name": "test.txt", "bucket_name": "test-bucket"},
    )
    assert response.status_code == 200
    assert response.content == b"mock file content"
    mock_s3.download_file.assert_called_once_with("test-bucket", "test.txt")

def test_download_file_bucket_not_exists(mock_s3):
    mock_s3.bucket_exists.return_value = False
    response = client.post(
        "/files/download/",
        params={"object_name": "test.txt", "bucket_name": "test-bucket"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Bucket does not exist."}
    mock_s3.download_file.assert_not_called()
