import boto3
import datetime
import json

print('Loading function')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):

    # Print the input for logging
    print("Received event: " + json.dumps(event, indent=2))
    
    # Check for table name, table key, pathParams and body
    if 'tableName' not in event or 'tableKey' not in event or 'body' not in event or 'pathParams' not in event:
        raise Exception('API Mapping Error') #501
        
    # Default values
    item = None
    # Read out path parameters
    if event['tableKey'] in event['pathParams']:
        item = {}
        item[event['tableKey']] = event['pathParams'][event['tableKey']]
        
    # Check for invalid path input
    if item is None:
        raise Exception('Invalid Input Error') #400
    
    # Update timestamp
    event['body']['timestamp'] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    # Build up the update expressions
    expressionPairs = []
    expressionAttrNames = {}
    expressionAttrValues = {}
    for key, val in event['body'].items():
        if key == event['tableKey']:
            continue # skip tableKey 
        expressionNameKey = '#' + key
        expressionValueKey = ':' + key
        expressionPairs.append(expressionNameKey + ' = ' + expressionValueKey)
        expressionAttrNames[expressionNameKey] = key
        expressionAttrValues[expressionValueKey] = val
    updateExpression = "SET " + ', '.join(expressionPairs)
    print(updateExpression)
    print(expressionAttrNames)
    print(expressionAttrValues)
    # Make sure there are some updates to do
    if not expressionAttrNames or not expressionAttrValues:
        raise Exception('Invalid Input Error') #400
    
    # Perform put_item based on input parameters
    try:
        table = dynamodb.Table(event['tableName'])
        response = table.update_item(Key=item, UpdateExpression=updateExpression,
            ExpressionAttributeNames=expressionAttrNames, ExpressionAttributeValues=expressionAttrValues)
    except Exception as e:
        print(e)
        raise Exception('DynamoDB Error') #500
 
    print(response)
    return response
