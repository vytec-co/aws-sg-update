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
print("The Ingress rules are as follows: ")
if len(response['IpPermissions']) != 0:
for j in response['IpPermissions']:
    #print("IP Protocol: "+j['IpProtocol'])
    try:
    # print("PORT: "+str(j['FromPort']))
        if str(j['FromPort']) == str(port_no):
        print("PORT: "+str(j['FromPort']))
        for k in j['IpRanges']:
            # print("IP Ranges: "+k['CidrIp'])
            ipSet.add(k['CidrIp']) 
    except Exception:
        print("No value for ports and ip ranges available for this security group")
        continue
    if ipAddress not in ipSet:
        print("ip not exist and updating the rule with "+ipAddress)
        try:
            data = ec2.authorize_security_group_ingress(
                GroupId=i['GroupId'],
                IpPermissions=[
                    {'IpProtocol': 'tcp',
                    'FromPort': port_no,
                    'ToPort': port_no,
                    'IpRanges': [{'CidrIp': ipAddress, 'Description' : description}]}
                ])
            ipSet.add(ipAddress)
        except Exception:
            print("Given IP is not proper format and should be 0.0.0.0/0 format")
            continue
    else:
        print("ip already exist:"+ipAddress)
    print("ip rules are:")
    print(ipSet)
else:
try:
    data = ec2.authorize_security_group_ingress(
        GroupId=i['GroupId'],
        IpPermissions=[
            {'IpProtocol': 'tcp',
            'FromPort': port_no,
            'ToPort': port_no,
            'IpRanges': [{'CidrIp': ipAddress, 'Description' : description}]}
        ])
    ipSet.add(ipAddress)
    print("ip rules are:")
    print(ipSet)
except Exception:
    print("Given IP is not proper format and should be 0.0.0.0/0 format")
    continue