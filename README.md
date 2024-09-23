# FastAPI S3 File Service

This project is a simple FastAPI application that provides endpoints for uploading and downloading files to and from an S3-compatible storage service.

## Project Structure

- `app/main.py`: Entry point for the FastAPI application.
- `app/api/file_service.py`: Contains the API endpoints for file upload and download.
- `app/services/s3_client.py`: Contains a client wrapper for interacting with the S3 service.
- `app/core/config.py`: Contains the application configuration settings.
- `test_file_service.py`: Test cases for the `file_service.py` module.

## Requirements

- Python 3.8+
- FastAPI
- boto3
- pydantic
- pytest (for testing)
- httpx (for testing)

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Copy the .env.example file to .env and setup your variables:
    ```
    cp .env.example .env
    ```

## Running the Application

1. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --host localhost --port 8000 --reload
    ```

2. The API will be available at `http://localhost:8000`.

## Endpoints

### 1. Upload File

- **URL**: `/upload`
- **Method**: `POST`
- **Parameters**:
  - `object_name` (query param): Name of the object to be stored.
  - `bucket_name` (query param): Name of the S3 bucket.
  - `file` (form-data): File to be uploaded.
- **Response**: 
  - `201`: File uploaded successfully.
  - `404`: Bucket does not exist.
  - `500`: Internal server error.

### 2. Download File

- **URL**: `/download/`
- **Method**: `POST`
- **Parameters**:
  - `object_name` (query param): Name of the object to be downloaded.
  - `bucket_name` (query param): Name of the S3 bucket.
- **Response**: 
  - `200`: Returns the file as a streaming response.
  - `404`: Bucket does not exist.
  - `500`: Internal server error.

## Running Tests

1. Run the tests using `pytest`:
    ```bash
    pytest test_file_service.py
    ```

2. The test file contains test cases for both file upload and download endpoints.
