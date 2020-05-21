# List IAM, S3 and EC2 using Client
#----------------------------------------
import boto3

# List IAM
aws_mng_con = boto3.session.Session(profile_name='pythonAutomation')
iam_con = aws_mng_con.client('iam')
iam_list = iam_con.list_users()['Users']
print('------- IAM List -----------')
for iam in iam_list:
    print(iam['UserName'])

# List S3
s3_con = aws_mng_con.client('s3')
s3_list = s3_con.list_buckets()['Buckets']
print('------- S3 List -----------')
for s3 in s3_list:
    print(s3['Name'])

# List EC2
ec2_con = aws_mng_con.client('ec2')
ec2_list = ec2_con.describe_instances()['Reservations']
print('------- EC2 List -----------')
for each_instance in ec2_list:
    for each_ec2 in each_instance['Instances']:
        print(each_ec2['InstanceId'],each_ec2['State']['Name'])