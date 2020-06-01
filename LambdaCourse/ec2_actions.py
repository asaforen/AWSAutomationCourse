import boto3
import sys

aws_mng_con = boto3.session.Session(profile_name='pythonAutomation') # we can add ,region_name=''
ec2_con_re  = aws_mng_con.resource(service_name="ec2")
ec2_con_cli = aws_mng_con.client(service_name="ec2")

while True:
    print("This script performs the follwing actions on EC2:")
    print("""
           1. List all EC2s
           2. Start
           3. Stop
           4. Terminate
           5. Exit """)
    opt=int(input("Enter your option: "))
    if opt == 1:
        for each_ec2 in ec2_con_re.instances.all():
            # print(dir(each_ec2)) # -- to list all the options
            print(each_ec2.instance_id)
    elif opt == 2:
        instance_id = input("Please type instance ID: ")
        print(f"Starting instance_ID {instance_id}")
        instance = ec2_con_re.Instance(instance_id)
        instance.start()
        waiter=ec2_con_cli.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])
        print("Now your ec2 instace is up and running")
    elif opt == 3:
        instance_id = input("Please type instance ID: ")
        print(f"Stoping instance_ID {instance_id}")
        instance = ec2_con_re.Instance(instance_id)
        instance.stop()
        waiter=ec2_con_cli.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id])
        print("Your ec2 instace is stopped")
    elif opt == 4:
        instance_id = input("Please type instance ID: ")
        print(f"Terminate instance_ID {instance_id}")
        instance = ec2_con_re.Instance(instance_id)
        instance.terminate()
        waiter=ec2_con_cli.get_waiter('instance_terminated')
        waiter.wait(InstanceIds=[instance_id])
        print("Your ec2 instace is Terminated")
    elif opt == 5:
        print("Thank you, Good Bye.")
        sys.exit()
    else:
        print("Invalid Option, Please type again: ")