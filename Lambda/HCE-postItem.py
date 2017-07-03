import boto3
import datetime
import json
import uuid

print('Loading function')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):

    # Print the input for logging
    print("Received event: " + json.dumps(event, indent=2))
    
    # Check for table name, table key, and body
    if 'tableName' not in event or 'tableKey' not in event or 'body' not in event:
        raise Exception('API Mapping Error') #501
        
    # Check for valid body parameters
    if 'name' not in event['body']:
        raise Exception('Invalid Input Error') #400
    
    # Add UUID and timestamp
    event['body'][event['tableKey']] = str(uuid.uuid4())
    event['body']['timestamp'] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    # Perform put_item based on input parameters
    try:
        table = dynamodb.Table(event['tableName'])
        response = table.put_item(Item=event['body'])
    except Exception as e:
        print(e)
        raise Exception('DynamoDB Error') #500
 
    print(response)
    return response
