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
        eval(args.function)()
    except Exception as e:
        print("Please enter parameter as add | update | list | delete"+str(e))

def add():
    print("called add function")
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
            for i in response['SecurityGroups']:
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
                            print("No value for ports and ip ranges available for this security group"+str(e))
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

def update():
    print("called update function")
    # delete()
    # add()

def list():
    print("called list function")
    ipSet = set()
    client = boto3.client('ec2')
    response = client.describe_security_groups(
        GroupNames=[
            'testgroup',
        ],
    )
    for i in response['SecurityGroups']:
        if len(i['IpPermissions']) != 0:
            for j in i['IpPermissions']:
                #print("IP Protocol: "+j['IpProtocol'])
                try:
                # print("PORT: "+str(j['FromPort']))
                    if str(j['FromPort']) == str(port_no):
                        #print("PORT: "+str(j['FromPort']))
                        for k in j['IpRanges']:
                            # print("IP Ranges: "+k['CidrIp'])
                            ipSet.add(k['CidrIp']) 
                except Exception as e:
                    print("No value for ports and ip ranges available for this security group"+e)
                    continue
    print(ipSet) 
def delete():
    print("called delete function")

if __name__ == '__main__':
    main()
