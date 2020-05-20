# coding: utf-8
import boto3
#session = boto3.Session(profile_name='default')
client = boto3.client('ec2')

def associate_iam_instance_profile(id):
    response = client.associate_iam_instance_profile(
        IamInstanceProfile={
            'Name': 'awsrole-ec2-ssm',
        },
        InstanceId= id,
    )

    print(response)