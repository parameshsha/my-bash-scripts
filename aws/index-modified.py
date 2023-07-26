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
response = s3_client.put_object(
    Body=open("index.py", "r").read(),
    Bucket= 's3bucketjune215',
     Key='index-modified.py',
)
print(response)
