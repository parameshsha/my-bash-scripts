import boto3

s3_client = boto3.client('s3', 
    aws_access_key_id="AKIA5DL3FD555MEDRMAI",
    aws_secret_access_key="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",
)

#response = s3_client.create_bucket(
#    Bucket= 's3bucketjune215',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'ap-south-1',
#    }

#)
#response = s3_client.put_object(
#    Body=open("index.py", "r").read(),
#    Bucket= 's3bucketjune215',
#     Key='index-modified.py',
#)

#response = s3_client.get_object(
#    Bucket='s3bucketjune215',
#     Key='index-modified.py',
#)
#data = response.get("Body").read().decode()
#file = open("index-modified.py", "w")
#file.writelines(data)
#file.close()

#response = s3_client.list_buckets()

#buckets = response.get("Buckets")
#print(len(buckets))
#print(buckets)

#response = s3_client.list_objects(
#    Bucket ='s3bucketjune215'
#)
#objects = response.get("Contents")
#print(len(objects))
#print(objects)
response = s3_client.delete_object(
    Bucket ='s3bucketjune215',
    key ='index-modified.py',

)
print(response)


