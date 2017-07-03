import boto3
import json

print('Loading function')
client = boto3.client('dynamodb')


def lambda_handler(event, context):

    # Print the input for logging
    print("Received event: " + json.dumps(event, indent=2))
    
    # Check for table name, table key, and queryParams
    if 'tableName' not in event or 'tableKey' not in event or 'queryParams' not in event:
        raise Exception('API Mapping Error') #501
        
    # Default values
    limit = 50
    lastKey = None
    # Read out query parameters
    if 'limit' in event['queryParams']:
        limit = int(event['queryParams']['limit'])
    if 'lastKey' in event['queryParams']:
        lastKey = {}
        lastKey[event['tableKey']] = {}
        lastKey[event['tableKey']]['S'] = event['queryParams']['lastKey']

    # Perform scans based on input parameters
    try:
        if lastKey is None:
            response = client.scan(TableName=event['tableName'], Limit=limit, Select='ALL_ATTRIBUTES')
        else:
            response = client.scan(TableName=event['tableName'], Limit=limit, Select='ALL_ATTRIBUTES', ExclusiveStartKey=lastKey)
    except Exception as e:
        print(e)
        raise Exception('DynamoDB Error') #500
    
    # Check for an empty response
    print(response)
    if 'Item' not in response and 'Items' not in response:
        raise Exception('Not Found Error') #404
    return response
