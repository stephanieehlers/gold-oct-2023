import boto3


s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket = 'sehlers-boto3-10292023') # if you just want a specific file you can do Prefix='txtfileyouwant'


for content in response ['Contents']:
    if('.txt' in content['Key'][-4:]):  # this will print all files with .txt
         print(content['Key'])