import boto3

def list_policies():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="AWS"):
        # print(response)
        for policy in response['Policies']:
            print("{} - {} ".format(policy["PolicyName"],policy['Arn']))
list_policies()