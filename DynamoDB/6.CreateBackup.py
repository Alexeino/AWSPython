import boto3
from pprint import pprint

db = boto3.client('dynamodb')
# response = db.create_backup(
#     TableName = 'Article',
#     BackupName = 'ArticleBackup'
# )
response = db.delete_backup(
    BackupArn = 'arn:aws:dynamodb'

)
pprint(response)