import boto3

def create_access_key(userName):
    iam = boto3.client("iam")

    res = iam.create_access_key(
        UserName = userName
    )
    key = res['AccessKey']['AccessKeyId']
    secret = res['AccessKey']['SecretAccessKey']
    print("Access Key - ",key)
    print("Secret Key - ",secret)


# create_access_key("user1")

def update_access_key(userName):
    iam = boto3.client("iam")

    iam.update_access_key(
        AccessKeyId = "AKIAW6GQHN44354KS6CJ",
        Status = 'Inactive',
        UserName = userName

    )
update_access_key("user1")