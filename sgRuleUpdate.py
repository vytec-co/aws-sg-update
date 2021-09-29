import boto3
ipSet = set()
ec2 = boto3.client('ec2',region_name='us-east-2')
response = ec2.describe_security_groups()
securityGroup = input("Enter security Group Name:- ")
print("Entered,", securityGroup,"\b!")
ipAddress = input("Enter Ip address(format:- 0.0.0.0/0) to add into security Group rule:- ")
print("Entered,", ipAddress,"\b!")
#print(response)
for i in response['SecurityGroups']:
    #print("Security Group Name: "+i['GroupName'])
    if i['GroupName'] == securityGroup:
       print("Security Group Name: "+i['GroupName'])
       print("The Ingress rules are as follows: ")
       for j in i['IpPermissions']:
          #print("IP Protocol: "+j['IpProtocol'])
          try:
           # print("PORT: "+str(j['FromPort']))
            if str(j['FromPort']) == '80':
               print("PORT: "+str(j['FromPort']))
               for k in j['IpRanges']:
                 # print("IP Ranges: "+k['CidrIp'])
                  ipSet.add(k['CidrIp']) 
          except Exception:
            print("No value for ports and ip ranges available for this security group")
            continue
       #print(ipSet)
       #ip = '12.0.0.0/8'
       if ipAddress not in ipSet:
           print("ip not exist and updating the rule with "+ipAddress)
           try:
             data = ec2.authorize_security_group_ingress(
                  GroupId=i['GroupId'],
                  IpPermissions=[
                      {'IpProtocol': 'tcp',
                       'FromPort': 80,
                       'ToPort': 80,
                       'IpRanges': [{'CidrIp': ipAddress}]}
                  ])
             ipSet.add(ipAddress)
           except Exception:
             print("Given IP is not proper format and should be 0.0.0.0/0 format")
             continue
       else:
           print("ip already exist:"+ipAddress)
       print("ip rules are:")
       print(ipSet)
