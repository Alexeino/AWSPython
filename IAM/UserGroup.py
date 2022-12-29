import boto3

def create_group(group_name):
    iam = boto3.client("iam")
    iam.create_group(GroupName=group_name)

def attach_group_policy(groupName,policyArn):
    iam = boto3.client("iam")
    respones = iam.attach_group_policy(
        GroupName = groupName,
        PolicyArn = policyArn
    )
    print(respones)

def detach_group_policy(groupName,policyArn):
    iam = boto3.client("iam")
    response = iam.detach_group_policy(
        GroupName = groupName,
        PolicyArn = policyArn
    )
    print(response)

def add_user_to_group(groupName,userName):
    iam = boto3.client("iam")
    response = iam.add_user_to_group(
        GroupName = groupName,
        UserName = userName
    )
    print(response)

# create_group("TestGroup")
# attach_group_policy("TestGroup","arn:aws:i am::477178064697:policy/pyFullAccess")
# detach_group_policy("TestGroup","arn:aws:iam::477178064697:policy/pyFullAccess")
add_user_to_group("TestGroup","user1")