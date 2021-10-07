import argparse
import sys
import boto3
def main():
    if (len(sys.argv)-1 == 0):
         print("Please enter parameter as add | update | list | delete")
         quit()
    parser = argparse.ArgumentParser()
    parser.add_argument('function', type=str, help='function to call')
    args = parser.parse_args()
    if (args != ""):
        try:  
            eval(args.function)()
        except:
          print("Please enter parameter as add | update | list | delete")

def add():
    print("called add function")
    ipSet = set()
    ec2 = boto3.client('ec2',region_name='us-east-2')
    response = ec2.describe_security_groups()
    securityGroup = input("Enter security Group Name:- ")
    print("Entered security group ,", securityGroup,"\b!")
    raw_port_no = input("Enter port number to add into security Group rule:- ")
    port_no = int(raw_port_no)
    print("Entered,", port_no,"\b!")
    ipAddress = input("Enter Ip address(format:- 0.0.0.0/0) to add into security Group rule:- ")
    print("Entered,", ipAddress,"\b!")
    description = input("Enter Description to add into security Group rule:- ")
    print("Entered,", description,"\b!")
    #print(response)
    client = boto3.client('ec2',region_name='us-east-2')
    response = client.describe_security_groups(
        GroupNames=[
            'testgroup',
        ],
    )
    for i in response['SecurityGroups']:
        #print("Security Group Name: "+i['GroupName'])
        # if i['GroupName'] == securityGroup:
        print("Security Group Name: "+i['GroupName'])
        print("The Ingress rules are as follows: ")
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

def update():
    print("called update function")
    delete()
    add()

def list():
    print("called list function")

def delete():
    print("called delete function")

if __name__ == '__main__':
    main()
