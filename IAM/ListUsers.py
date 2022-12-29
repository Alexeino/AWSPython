import boto3

def list_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    print("Paginator object - ",paginator)
    for response in paginator.paginate():
        # print("Response - ",response)
        for user in response['Users']:
            ARN = user['Arn']
            username = user['UserName']
            print("{} - ARN {}".format(username,ARN))



list_users()