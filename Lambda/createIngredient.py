import boto3
import datetime
import json
import uuid

print('Loading function')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CookieExperiment-Ingredients')


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
    if 'name' not in event['body']:
        return respond('Input Error')
    
    event['body']['ingId'] = str(uuid.uuid4())
    event['body']['timestamp'] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    try:
        response = table.put_item(Item=event['body'])
    except Exception as e:
        print(e)
        return respond('DynamoDB Error')
 
    return respond(None, response)
