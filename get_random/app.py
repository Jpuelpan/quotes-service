import json
import os
import boto3
import uuid
import time

QUOTES_TABLE = os.getenv('QUOTES_TABLE')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(QUOTES_TABLE)

def lambda_handler(event, context):
    lastKeyEvaluated = {
        "id": str(uuid.uuid1()),
        "createdAt": 0
    }

    result = table.scan(
        ExclusiveStartKey=lastKeyEvaluated,
        Limit=1
    )

    body = {}

    if result['Count'] > 0:
        item = result['Items'][0]
        item['createdAt'] = int(item['createdAt'])
        body = item

    return {
        "statusCode": 200,
        "body": json.dumps(body),
   }

