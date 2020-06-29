import boto3
aws_mag_con=boto3.session.Session(profile_name="pythonAutomation")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="eu-west-1")
#vpc_con_re= ec2_con_re.vpc('id')
vpc = []
for each_vpc in ec2_con_re.vpcs.all():
    vpc = ec2_con_re.Vpc(each_vpc.id)
    print(each_vpc.vpc_id, each_vpc.cidr_block, each_vpc.state)