import boto3
mybuckets = []
client = boto3.client('s3')
response = client.list_buckets()
#print(response)
print(type(response))
print(type(response.get("ResponseMetadata")))
print(type(response["Buckets"]))
buckets = response["Buckets"]
#print(buckets)
print(len(buckets))
for item in buckets:
    print(item.get("Name"))
    mybuckets.append(item.get("Name"))
    print("my buckets list is : ",mybuckets )
    