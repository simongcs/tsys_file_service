import boto3
from botocore.exceptions import ClientError, NoCredentialsError


class S3Client:
    def __init__(self, endpoint_url, aws_access_key_id, aws_secret_access_key, region_name):
        self.s3 = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def upload_file(self, bucket_name, object_name, file_content):
        try:
            self.s3.put_object(Bucket=bucket_name, Key=object_name, Body=file_content)
        except (NoCredentialsError, ClientError) as e:
            raise Exception(f"Failed to upload file: {e}")

    def download_file(self, bucket_name, object_name):
        try:
            response = self.s3.get_object(Bucket=bucket_name, Key=object_name)
            return response['Body'].read()
        except (NoCredentialsError, ClientError) as e:
            raise Exception(f"Failed to download file: {e}")
        
    def bucket_exists(self, bucket_name):
        try:
            self.s3.head_bucket(Bucket=bucket_name)
            return True
        except ClientError:
            return False
