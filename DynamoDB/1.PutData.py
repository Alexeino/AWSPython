import boto3

db = boto3.resource("dynamodb")
table = db.Table("employee")

item = {
     'emp_id':'1',
     'name':'Ankit',
     'age':24,
 }
response = table.put_item(Item=item)
print(response)