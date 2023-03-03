import boto3
from pprint import pprint
db = boto3.client('dynamodb')

res = db.update_table(
    TableName='employee',
    BillingMode='PROVISIONED',
    
    ProvisionedThroughput = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    }
)

pprint(res)