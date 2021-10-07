import boto3
ipSet = set()
client = boto3.client('ec2',region_name='us-east-2')
response = client.describe_security_groups(
    GroupNames=[
        'testgroup',
    ],
)
print(response)
print("Security Group Name: "+response['GroupName'])
print("The Ingress rules are as follows: "+response['IpPermissions'])
