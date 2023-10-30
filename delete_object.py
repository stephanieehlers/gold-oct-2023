import boto3

bucket = 'sehlers-boto3-10292023'
key = 'texttest.txt'

s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket=bucket,
    Key=key,
)

#this is how you delete objects from the bucket