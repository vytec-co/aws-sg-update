import argparse
import sys
import boto3
import json
def main():
    if (len(sys.argv)-1 == 0):
         print("Please enter parameter as add | update | list | delete")
         quit()
    parser = argparse.ArgumentParser()
    parser.add_argument('function', type=str, help='function to call')
    args = parser.parse_args()
    try:  
        securityGroup = input("Enter security Group Name:- ")
        print("Entered security group ,", securityGroup,"\b!")
        eval(args.function)(securityGroup)
    except Exception as e:
        print("Please enter parameter as add | update | list | delete "+str(e))

def add(securityGroup):
    with open("addresses", "r") as my_file:
        for line in my_file:
            port_no = int(line.split()[0])
            ipAddress = line.split()[1]
            description = line.split()[2]
            client = boto3.client('ec2')
            response = client.describe_security_groups(
                GroupNames=[
                    securityGroup,
                ],
            )
            for i in response['SecurityGroups']:
                ipSet = set()
                if len(i['IpPermissions']) != 0:
                    for j in i['IpPermissions']:
                        if str(j['FromPort']) == str(port_no):
                            for k in j['IpRanges']:
                                ipSet.add(k['CidrIp']) 
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
                            print("sg rule updated - "+str(ipAddress))
                        except Exception as e:
                            print("Given IP is not proper format and should be 0.0.0.0/0 format "+str(e))
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
                    except Exception as e:
                        print("Given IP is not proper format and should be 0.0.0.0/0 format "+str(e))
                        continue    

def update(securityGroup):
    delete(securityGroup)
    add(securityGroup)

def list(securityGroup):
    client = boto3.client('ec2')
    response = client.describe_security_groups(
        GroupNames=[
            securityGroup,
        ],
    )
    for i in response['SecurityGroups']:
        if len(i['IpPermissions']) != 0:
            for j in i['IpPermissions']:
                for k in j['IpRanges']:
                    print(j['FromPort'], k['CidrIp'], k['Description'])                 
def delete(securityGroup):
    with open("addresses", "r") as my_file:
        for line in my_file:
            port_no = int(line.split()[0])
            ipAddress = line.split()[1]
            description = line.split()[2]
            client = boto3.client('ec2')
            response = client.describe_security_groups(
                GroupNames=[
                    securityGroup,
                ],
            )
            for i in response['SecurityGroups']:
                ipSet = set()
                if len(i['IpPermissions']) != 0:
                    for j in i['IpPermissions']:
                        if str(j['FromPort']) == str(port_no):
                            for k in j['IpRanges']:
                                ipSet.add(k['CidrIp'])             
                    if ipAddress in ipSet:
                        print("ip exist and updating the rule with "+ipAddress)
                        try:
                            data = client.revoke_security_group_ingress(
                                GroupId=i['GroupId'],
                                CidrIp=ipAddress,
                                IpProtocol='tcp',
                                FromPort=port_no,
                                ToPort=port_no
                            )
                            print("sg rule deleted - "+str(ipAddress))
                        except Exception as e:
                            print("Given IP is not proper format and should be 0.0.0.0/0 format "+str(e))
                            continue
                    else:
                        print("ip address not exist: "+ipAddress)
                else:
                    print("ip address not exist: "+ipAddress)
if __name__ == '__main__':
    main()
