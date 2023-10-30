import boto3

s3 = boto3.client('s3')


s3.upload_file('texttest.txt', 'sehlers-boto3-10292023', 'texttest_upload.txt', ExtraArgs={'ContentType':'text/plain'})   