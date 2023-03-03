import boto3
from pprint import pprint

db = boto3.client("dynamodb")
res = db.list_tables()
pprint(res['TableNames'])