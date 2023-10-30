import boto3

subnet_id = 'subnet-028e623f25765ab52'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

