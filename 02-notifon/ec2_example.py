ec2 = session.resource('ec2')
session = boto3.Session(profile_name='pythonAutomation')
import boto3

session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')

instances = ec2.create_instances(ImageId=img.id,InstanceType='t2.micro', MaxCount=1, MinCount=1,KeyName=key.key_name,SubnetId='subnet-045a76384c32c9d1f')
img = ec2.Image('ami-06ce3edf0cff21f07')
key_pair_info = ec2.KeyPair('python_automation_key')
key = key_pair_info.name

instances = ec2.create_instances(ImageId=img.id,InstanceType='t2.micro', MaxCount=1, MinCount=1,KeyName=key,SubnetId='subnet-045a76384c32c9d1f')
inst = instances[0]
inst.wait_until_running

inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup([0]['GroupId'])
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp':'79.178.196.179/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp':'79.178.196.179/32'}]}])
inst.public_dns_name
