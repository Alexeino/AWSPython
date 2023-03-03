import boto3

db = boto3.resource("dynamodb")
table = db.Table('employee')

def load_items1():
    with table.batch_writer() as batch:
        batch.put_item(Item={
            'emp_id':'2',
            'name':'Manish',
            'age':24
        })
        batch.put_item(Item={
            'emp_id': '3',
            'name': 'Jatin',
            'age': 25
        })

# method 2 using for loop for large amount of data
with table.batch_writer() as batch:
    for i in range(10):
        batch.put_item(Item={})