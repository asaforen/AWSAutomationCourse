import boto3
from pprint import pprint

aws_mng_con = boto3.session.Session(profile_name="pythonAutomation")
ec2_con_re = aws_mng_con.resource(service_name="ec2", region_name="eu-west-1")

filter_vol = {"Name":"tag:Dev", "Values":['Backup','backup']}
list_of_volumes = []
for each_ebs in ec2_con_re.volumes.filter(Filters=[filter_vol]):
    list_of_volumes.append(each_ebs.id)

print(f"the list of volume id's: {list_of_volumes}")