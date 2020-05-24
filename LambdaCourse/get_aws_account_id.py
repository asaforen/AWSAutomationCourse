import boto3

aws_mng_con = boto3.session.Session(profile_name='pythonAutomation') # we can add ,region_name=''
sts_con_id = aws_mng_con.client('sts')

response = sts_con_id.get_caller_identity()
print("Account ID: ", response['Account'], " User ID: ", response['UserId'])