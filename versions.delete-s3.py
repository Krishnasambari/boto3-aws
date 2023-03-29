import boto3
import time
s3 = boto3.resource('s3')
bucket = s3.Bucket("cmstage-prod")
bucket.object_versions.delete()

# if you want to delete the now-empty bucket as well, uncomment this line:
#bucket.delete()AKIATS7YLYJSFKOCDRO4