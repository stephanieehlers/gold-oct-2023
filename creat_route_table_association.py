import boto3

route_table_id = 'rtb-06f18452a81d61823'
subnet_id = 'subnet-028e623f25765ab52'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id ,
)

print(association['AssociationId'])