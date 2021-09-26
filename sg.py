import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
try:
    for sg in ec2.describe_security_groups()['SecurityGroups']:
        print(sg['GroupName'])
        if sg['GroupName'] == 'testgroup':
           security_group_id = sg['GroupName'] 
           break
        else:
            security_group_id = "NotExist" 
    print('Security Group exist status  %s in vpc %s.' % (security_group_id, vpc_id))

    if security_group_id == 'NotExist':
            response = ec2.create_security_group(GroupName='testgroup',
                                                Description='test descroiption',
                                                VpcId=vpc_id)
            security_group_id = response['GroupId']
            print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
    # data = ec2.authorize_security_group_ingress(
    #     GroupId=security_group_id,
    #     IpPermissions=[
    #         {'IpProtocol': 'tcp',
    #          'FromPort': 80,
    #          'ToPort': 80,
    #          'IpRanges': [{'CidrIp': '10.0.0.0/0'}]},
    #         {'IpProtocol': 'tcp',
    #          'FromPort': 22,
    #          'ToPort': 22,
    #          'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    #     ])
    data = client.modify_security_group_rules(
    GroupId=security_group_id,
    SecurityGroupRules=[
        {
            'SecurityGroupRuleId': 'string',
            'SecurityGroupRule': {
                'IpProtocol': 'tcp',
                'FromPort': 123,
                'ToPort': 123,
                'CidrIpv4': '10.0.0.0/0',
                'ReferencedGroupId': security_group_id,
                'Description': 'abbcbcc'
            }
        },
    ],
    DryRun=False
)
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)
