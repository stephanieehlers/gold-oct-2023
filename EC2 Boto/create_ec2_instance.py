import boto3

ami_id = 'ami-036de4baa9dd8b764'
key_pair_name = 'Key from boto3'
security_group_id = 'sg-022edc0f41d7c2ee7'

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id,
    ]
    
)

print(response['Instances'][0]['InstanceId'])