import boto3

class S3Client:
    def __init__(self):
        self.client = boto3.client('s3') 

    def get_object(self, bucket, key):
        return self.client.get_object(
            Bucket=bucket,
            Key=key
        )['Body']