import boto3
from pprint import pprint
db = boto3.client("dynamodb")

res = db.describe_table(
    TableName = 'employee'
)
pprint(res)