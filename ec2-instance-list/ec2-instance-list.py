import boto3
import click

session=boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.command()
def list_instances():
    "List all the Ec2 instances"
    for data in ec2.instances.all():
        print(",".join((
            data.id,
            data.instance_type,
            data.placement['AvailabilityZone'],
            data.state['Name'],
            data.public_dns_name)))
    return

if __name__ == '__main__':
     list_instances()
