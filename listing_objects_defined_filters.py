import boto3

def filter_objects_extension(client, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response ['Contents']:
        if(extension in content['Key'][-(len(extension)):]):  
            keys.append(content['Key'])
   
    return keys        
        
s3 = boto3.client('s3')

response = filter_objects_extension(s3, 'sehlers-boto3-10292023', '.txt')

print(response)

