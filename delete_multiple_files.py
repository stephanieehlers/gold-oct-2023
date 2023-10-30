import boto3

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key,
    )   
    
    return response
    
def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
            
    response = client.delete_objects(
         Bucket=bucket,
        Delete={
            'Objects':objects
        }
    )
    
    return response

bucket = 'sehlers-boto3-10292023'
key = 'texttest.txt'

s3 = boto3.client('s3')

keys = ['.txt', '.txt'] # put the file names you want to delete here

delete_object(s3, bucket, key)