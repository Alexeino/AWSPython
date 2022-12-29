import boto3

def attach_policy(policyArn,username):
    iam = boto3.client("iam")
    response = iam.attach_user_policy(
        UserName = username,
        PolicyArn = policyArn
    )

    print(response)

attach_policy("arn:aws:iam::477178064697:policy/pyFullAccess","user1")