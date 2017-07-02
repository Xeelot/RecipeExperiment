import boto3
import json

print('Loading function')
client = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    limit = 50
    lastKey = None
    if 'limit' in event['queryParams']:
        limit = event['queryParams']['limit']
    if 'lastKey' in event['queryParams']:
        lastKey = {}
        lastKey['ingId'] = {}
        lastKey['ingId']['S'] = event['queryParams']['lastKey']

    try:
        if lastKey is None:
            response = client.scan(TableName='CookieExperiment-Ingredients',
                Limit=limit, Select='ALL_ATTRIBUTES')
        else:
            response = client.scan(TableName='CookieExperiment-Ingredients',
                Limit=limit, Select='ALL_ATTRIBUTES', ExclusiveStartKey=lastKey)
    except Exception as e:
        print(e)
        return respond('DynamoDB Error')
 
    return respond(None, response)
