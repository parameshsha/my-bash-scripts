import boto3

client = boto3.client('ec2')
response = client.describe_instances()
print(type(response))

Reservations = response.get("Reservations")[0]
print(type(Reservations))
Instances = Reservations.get("Instances")
print(type(Instances))
for items in Instances: 
    print(type(items))
    print(items.get("PrivateIpAddress"))
    if items.get("State").get("Names") == "running":
        print(items["NetworkInterfaces"][0]["Association"]["publicIp"])
    
    