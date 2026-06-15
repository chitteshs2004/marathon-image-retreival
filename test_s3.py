import boto3
from botocore.exceptions import ClientError

import os

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION', 'us-east-1')
)

bucket = 'chittesh-bucket'

try:
    objs = s3.list_objects_v2(Bucket=bucket)
    print(f"[OK] ListObjects: {objs.get('KeyCount', 0)} objects in bucket")
except ClientError as e:
    print(f"[FAIL] ListObjects: {e}")

try:
    s3.put_object(Bucket=bucket, Key='_test_.txt', Body=b'test')
    print("[OK] PutObject: write access confirmed")
    s3.delete_object(Bucket=bucket, Key='_test_.txt')
    print("[OK] DeleteObject: delete access confirmed")
except ClientError as e:
    print(f"[FAIL] PutObject: {e}")
