import json
import boto3

def lambda_handler(event, context):
    
    print(event)
    vol = event["resources"][0]
    print(vol)
    print(type(vol))
    txt = vol.split('/')
    vol_id = txt[1]
    print(vol_id)
    
    ec2_client = boto3.client('ec2')
    
    response =ec2_client.modify_volume(
    
    VolumeId =vol_id,
  
    VolumeType='gp3',
    
)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
