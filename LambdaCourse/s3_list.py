import boto3

aws_mng_con = boto3.session.Session(profile_name="pythonAutomation")
s3_list_buk = aws_mng_con.resource('s3')

for each_buk in s3_list_buk.buckets.all():
    print(each_buk.name)