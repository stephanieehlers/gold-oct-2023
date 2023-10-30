import boto3 

route_table_id = 'rtb-06f18452a81d61823'
internet_gateway_id = 'igw-07083744528bf92f0'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
