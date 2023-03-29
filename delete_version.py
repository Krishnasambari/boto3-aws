import boto3
client = boto3.client('s3')
s3 = boto3.resource("s3")
bucket=s3.Bucket('cmstage-prod')
bucket.object_versions.all().delete() 