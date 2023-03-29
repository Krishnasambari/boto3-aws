import boto3

# Define the S3 client
s3 = boto3.client('s3')

# Set the bucket and prefix of the subfolder to delete
bucket_name = 'srichaitanyappbkp'
prefix = 'prod/assets/uploads/students_profile_pic/'

# Retrieve all object versions to delete
versions = s3.list_object_versions(Bucket=bucket_name, Prefix=prefix)['Versions']

# Create a list of objects and their versions to delete
objects_to_delete = [{'VersionId': obj['VersionId'], 'Key': obj['Key']} for obj in versions]

# Delete all object versions
s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects_to_delete})

# Delete the subfolder
s3.delete_object(Bucket=bucket_name, Key=prefix)

# Print the deleted objects
for obj in objects_to_delete:
    print(f"Deleted {obj['Key']} with version ID {obj['VersionId']}")
