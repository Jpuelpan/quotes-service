import json
import os
import boto3

QUOTES_TABLE = os.getenv('QUOTES_TABLE')

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world "
        }),
   }
