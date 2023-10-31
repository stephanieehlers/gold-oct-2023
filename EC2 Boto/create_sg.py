import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='SG from boto3',
    GroupName='boto3-security-group',
    VpcId='vpc-0ec0a825add7361ae',
)

print(response['GroupId'])