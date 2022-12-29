import boto3

def delete_user(username):
    iam = boto3.client("iam")

    # iam.detach_user_policy(
    #     UserName = username,
    #     PolicyArn = "arn:aws:iam::477178064697:policy/pyFullAccess"
    # )
    # iam.delete_login_profile(
    #     UserName = username
    # )
    res = iam.delete_user(
        UserName = username
    )
    print(res)

delete_user("user2")