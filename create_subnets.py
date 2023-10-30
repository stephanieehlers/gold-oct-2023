import boto3

cidr_block = '12.0.1.0/24'
vpc_id = 'vpc-00e64d7469e86edf0'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

print(subnet['Subnet']['SubnetId'])