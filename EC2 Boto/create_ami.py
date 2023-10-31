import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-071cf0bdd87605a8b',
    Name='Go to Ami'
)

print(response['ImageId'])