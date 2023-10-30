import boto3

vpc_id = 'vpc-00e64d7469e86edf0'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

