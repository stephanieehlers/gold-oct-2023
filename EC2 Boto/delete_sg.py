import boto3

sg_id = 'sg-022edc0f41d7c2ee7'

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId=sg_id
)

print(response)