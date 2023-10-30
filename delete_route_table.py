import boto3

route_table_id = 'rtb-06f18452a81d61823'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)
