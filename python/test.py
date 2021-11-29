import boto3
import json
ipSet = set()
json_data = []
with open('addresses.json') as json_file:
  json_data = json.load(json_file)
  for item in json_data:
    #for data_item in item['data']:
    print(item['ip_prefix'])
    print(item['description'])
    ipAddress = item['ip_prefix']
    description = item['description']
    port_no = 443
    client = boto3.client('ec2')
    response = client.describe_security_groups(
        GroupNames=[
            'testgroup',
        ],
    )
    print("1")
    for i in response['SecurityGroups']:
        print(i['GroupId'])
        if len(i['IpPermissions']) != 0:
            for j in i['IpPermissions']:
                #print("IP Protocol: "+j['IpProtocol'])
                try:
                # print("PORT: "+str(j['FromPort']))
                    if str(j['FromPort']) == str(port_no):
                        print("PORT: "+str(j['FromPort']))
                        for k in j['IpRanges']:
                            # print("IP Ranges: "+k['CidrIp'])
                            ipSet.add(k['CidrIp']) 
                except Exception as e:
                    print("No value for ports and ip ranges available for this security group"+e)
                    continue
                if ipAddress not in ipSet:
                    print("ip not exist and updating the rule with "+ipAddress)
                    try:
                        data = client.authorize_security_group_ingress(
                            GroupId=i['GroupId'],
                            IpPermissions=[
                                {'IpProtocol': 'tcp',
                                'FromPort': port_no,
                                'ToPort': port_no,
                                'IpRanges': [{'CidrIp': ipAddress, 'Description' : description}]}
                            ])
                        ipSet.add(ipAddress)
                    except Exception as e:
                        print("Given IP is not proper format and should be 0.0.0.0/0 format"+str(e))
                        continue
                else:
                    print("ip already exist:"+ipAddress)      
        else:
            try:
                print("rule update started:"+ipAddress)
                data = client.authorize_security_group_ingress(
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
            except Exception as e:
                print("Given IP is not proper format and should be 0.0.0.0/0 format"+str(e))
                continue
        print("ip rules are:")
        print(ipSet)    
    print("updated") 

