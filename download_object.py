import boto3

s3 = boto3.client('s3')

s3.download_file('sehlers-boto3-10292023', 'texttest_string.txt', 'texttest_string.txt')

#this is to download a file