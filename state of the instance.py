import boto3
ec2 = boto3.client('ec2',region_name='ap-south-1')
a = ec2.describe_instances()
for i in a['Reservations']:
    for j in i['Instances']:
     print ("Instance ID : "+j['InstanceId']+"      State of the instance :"+j['State']['Name'])
