import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='sehlers-boto3-10292023',
)

print(response)