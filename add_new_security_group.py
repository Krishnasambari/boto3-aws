import inquirer
import boto3

from botocore.exceptions import ClientError


Group_name = input("Please Enter a Group Name : ")
Description_Value = input("Ener the Description : ")
Ip_protocol = [
  inquirer.List('Selected Protocol',
                message="What Proctocl do you want use ?",
                choices=['tcp', 'udp'],
            ),
]
# print(Ip_protocol)
answers = inquirer.prompt(Ip_protocol)
# print(answers)
From_Port = int(input("Fron Port :"))
To_Port = int(input(" To Port : "))
Ip_Ranges = input(" CIDR:")

ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
    response = ec2.create_security_group(GroupName=Group_name,
                                         Description=Description_Value,
                                         VpcId=vpc_id)
    # 'SECURITY_GROUP_NAME', DESCRIPTION we can i 
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': answers['Selected Protocol'],
               
             'FromPort': From_Port,
             'ToPort': To_Port,
             'IpRanges': [{'CidrIp': Ip_Ranges}]}
        ]
    )
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)
