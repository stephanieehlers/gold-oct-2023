import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket='sehlers-boto3-10292023', Key='texttest_string.txt', Body='Hey this is a string', ContentType='text/plain')
