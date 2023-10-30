import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object',Params={'Bucket': 'sehlers-boto3-10292023','Key': 'texttest.txt'},ExpiresIn=300) # this is in seconds
 
print(response)