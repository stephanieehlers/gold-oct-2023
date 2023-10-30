import boto3
from list_objects import list_object_keys

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)
    
if __name__ == '__main__':  

    bucket = 'sehlers-boto3-10292023'
    key = 'texttest_string.txt'
    filename = 'texttest_string.txt'

    s3 = boto3.client('s3')

    keys = list_object_keys(s3, bucket) # use the prefix='folder/' to create a folder
    
    for key in keys:
        if '/' == key[-1]:  # this is what creates folders
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)
        

