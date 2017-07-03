import boto3
import json

print('Loading function')
client = boto3.client('dynamodb')


def lambda_handler(event, context):

    # Print the input for logging
    print("Received event: " + json.dumps(event, indent=2))
    
    # Check for table name, table key, and queryParams
    if 'tableName' not in event or 'tableKey' not in event or 'pathParams' not in event:
        raise Exception('API Mapping Error') #501
        
    # Default values
    item = None
    # Read out path parameters
    if event['tableKey'] in event['pathParams']:
        item = {}
        item[event['tableKey']] = {}
        item[event['tableKey']]['S'] = event['pathParams'][event['tableKey']]

    # Check for invalid path input
    if item is None:
        raise Exception('Invalid Input Error') #400
        
    # Perform delete_item based on input parameters
    try:
        response = client.delete_item(TableName=event['tableName'], Key=item)
    except Exception as e:
        print(e)
        raise Exception('DynamoDB Error') #500
 
    print(response)
    return response
