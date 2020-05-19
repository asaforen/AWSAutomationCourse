import boto3

aws_mng_con = boto3.session.Session(profile_name="pythonAutomation")
iam_con= aws_mng_con.resource('iam')
for each_user in iam_con.users.all():
    print(each_user.name)

