import boto3
from dotenv import load_dotenv
import os
from backend.config.path_configs import *

load_dotenv()

data_path = DATA_FOLDER_PATH
bucket_name = BUCKET_NAME

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key =os.getenv("AWS_SECRET_ACCESS_KEY_ID"),
    region_name = os.getenv("REGION_NAME")
)

def uploadFiles():
    for file_name in os.listdir(data_path):
        print(file_name)
        file_path = os.path.join(data_path,file_name)
        
        s3.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=file_name
        )


if __name__=="__main__":
    uploadFiles()