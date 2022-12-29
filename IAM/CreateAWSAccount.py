# Creating a Login Profile Start to End
import boto3

iam = boto3.client("iam")

def create_login(username):
    user = iam.create_user(UserName=username)
    policy = iam.attach_user_policy(UserName=username,PolicyArn="arn:aws:iam::477178064697:policy/pyFullAccess")
    profile_res = iam.create_login_profile(
        UserName = username,
        Password = "M#ni7h@2024",
        PasswordResetRequired = False
    )
    print(profile_res)

create_login("user2")