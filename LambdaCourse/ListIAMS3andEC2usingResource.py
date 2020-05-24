# List IAM, S3 and EC2 using Resource
#----------------------------------------
import boto3
import botostubs

aws_mng_con = boto3.session.Session(profile_name='pythonAutomation') # we can add ,region_name=''
iam_list = aws_mng_con.resource('iam')
ec2_list = aws_mng_con.resource('ec2')
s3_list = aws_mng_con.resource('s3')

# List IAM
for each_iam in iam_list.users.all():
    # print(dir(each_iam)) -- to list all the options
    print(each_iam.name)

# List ec2
for each_ec2 in ec2_list.instances.all():
    # print(dir(each_ec2)) # -- to list all the options
    print(each_ec2.instance_id)

# List S3
for each_bucket in s3_list.buckets.all():
    # print(dir(each_baclet)) -- to list all the options
    print(each_bucket.name)