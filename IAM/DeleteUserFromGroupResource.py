import boto3

def delete_user_from_group(username,groupName):
    iam = boto3.resource("iam")
    group = iam.Group(groupName)

    response = group.remove_user(
        UserName = username
    )
    print(response)

delete_user_from_group("user1","TestGroup")