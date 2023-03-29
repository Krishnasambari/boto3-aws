import boto3
# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
"""Output :
 keys-sriven
python-staging-skrishna  """ 
    
    
import sys
import boto3
import datetime
s3client = boto3.client(
 's3', 
 
 #aws_session_token='if token',
 )
allbuckets = s3client.list_buckets()
for bucket in allbuckets['Buckets']:
 print(bucket)
 
 """
 Output:
PS E:\CODING\PYTHON_AWS> python -u "e:\CODING\PYTHON_AWS\WORKSPACE.PY"
{'Name': 'keys-sriven', 'CreationDate': datetime.datetime(2022, 11, 29, 15, 28, 25, tzinfo=tzutc())}
{'Name': 'python-staging-skrishna', 'CreationDate': datetime.datetime(2022, 12, 22, 9, 40, 3, tzinfo=tzutc())} """