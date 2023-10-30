import boto3

s3 = boto3.client('s3')

with open('texttest.txt', 'rb') as f:
    s3.put_object(Bucket='sehlers-boto3-10292023', Key='texttest.txt', Body=f, ContentType='text/plain')

 