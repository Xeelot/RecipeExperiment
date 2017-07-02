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
    ingId = None
    if 'ingId' in event['pathParams']:
        ingId = {}
        ingId['ingId'] = {}
        ingId['ingId']['S'] = event['pathParams']['ingId']

    if ingId is None:
        return respond('Input Error')    
    try:
        response = client.get_item(TableName='CookieExperiment-Ingredients', Key=ingId)
    except Exception as e:
        print(e)
        return respond('DynamoDB Error')
 
    if 'Item' not in response:
        return respond('Not Found Error')
    return respond(None, response)
