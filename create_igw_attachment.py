import boto3

internet_gateway_id = 'igw-07083744528bf92f0'
vpc_id = 'vpc-00e64d7469e86edf0'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id ,
    VpcId=vpc_id,
)
