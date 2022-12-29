import boto3

iam = boto3.client("iam")
response = iam.detach_user_policy(
    UserName = "user1",
    PolicyArn = "arn:aws:iam::477178064697:policy/pyFullAccess"
)
print(dir(iam))
print(response)