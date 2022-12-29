import boto3

db = boto3.resource("dynamodb")
table = db.Table("employee")

table.put_item(Item={
    "emp_id":"2",
    "name":"Neelima",
    "age":23,
    "group":"Network Services",
    "band":"U2"
})