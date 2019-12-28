import json
import os
import boto3

QUOTES_TABLE = os.getenv('QUOTES_TABLE')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(QUOTES_TABLE)

def parse_items(item):
    item['createdAt'] = int(item['createdAt'])
    return item

def lambda_handler(event, context):
    result = table.scan(
        Limit=25
    )

    body = {
        'quotes': list(map(parse_items, result['Items']))
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body),
   }

