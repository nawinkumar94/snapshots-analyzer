import boto3

if __name__ == '__main__':
    session=boto3.Session(profile_name='snapshots-user')
    ec2=session.resource('ec2')
    
    for data in ec2.instances.all():
        print(data)
