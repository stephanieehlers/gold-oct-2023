import boto3


# How boto3 grants access
# AWS command line- default way that boto3 commo's with AWS
#IAM Role
#directly when calling the client

s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', aws_session_token='')

# you can call client and resource directly from session
session = boto3.Session()
s3 = boto3.client('s3') #client API like responses. More control over what we can do with AWS
s3 = session.client('s3')

s3 = boto3.resource('s3')
s3 = session.resource('s3')