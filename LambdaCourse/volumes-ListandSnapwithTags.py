import boto3
from pprint import pprint

aws_mng_con = boto3.session.Session(profile_name="pythonAutomation")
ec2_client = aws_mng_con.client(service_name='ec2', region_name="eu-west-1")
filter_vol = {"Name":"tag:Dev", "Values":['Backup','backup']}

list_of_vol = []
'''
for each_ebs in ec2_client.describe_volumes()['Volumes']:
    list_of_vol.append(each_ebs['VolumeId'])
'''
paginator = ec2_client.get_paginator('describe_volumes')
for each_vol in paginator.paginate(Filters=[filter_vol]):
    for each_vol_id in each_vol['Volumes']:
        list_of_vol.append(each_vol_id['VolumeId'])

waiter = ec2_client.get_waiter('snapshot_completed')
list_of_snap_ids = []
for each_id_snap in list_of_vol:
    pprint(f"Taking a snapshot of {each_id_snap}")
    response = ec2_client.create_snapshot(
                Description='New Snap with Script',
                VolumeId=each_id_snap)
    list_of_snap_ids.append(response['SnapshotId'])
waiter.wait(SnapshotIds=list_of_snap_ids)
print(f"Successfully complited the snapshot of the Volume id's: {list_of_vol} ")