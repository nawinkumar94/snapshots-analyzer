import boto3
import click
import botocore

session=boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

def filter_list(project):
    #Filter all the instances based on the instance tag value passed as a argument
    instances=[]
    if project:
        #'project' is a key of the instances
        filters=[{'Name':'tag:project','Values':[project]}]
        instances=ec2.instances.filter(Filters=filters)
    else:
        instances=ec2.instances.all()
    return instances

def has_pending_status(volume):
    status=list(volume.snapshots.all())
    return status and status[0].state=='pending'

#'group' in click will group the commands
@click.group()
def cli():
     "Group all the click group commands"

@cli.group()
def snapshots():
    "Group all the snapshots for the volumes command"

@snapshots.command('list')
@click.option("--project", default=None, help="List all the snapshots for volumes based on project")
@click.option("--all", "list_all" ,default=False ,is_flag=True, help="List all the snapshots for volumes based on project not only the recent one")

def list_snapshots(project,list_all):
     "List all the Ec2 snapshots for volumes"
     instances=filter_list(project)
     for data in instances:
         for volume in data.volumes.all():
             for snapshot in volume.snapshots.all():
                 print(",".join((
                 data.id,
                 volume.id,
                 snapshot.id,
                 snapshot.state,
                 snapshot.progress,
                 snapshot.start_time.strftime("%c"))))
                 if snapshot.state == 'completed' and not list_all:
                    break
     return

@cli.group()
def volumes():
    "Group all the volumes command"

@volumes.command('list')
@click.option("--project",default=None, help="List all the volumes based on project")
def list_volumes(project):
    "List all the Ec2 volumes for instances"
    instances=filter_list(project)
    for data in instances:
        for volume in data.volumes.all():
            print(",".join((
            data.id,
            volume.id,
            volume.state,
            str(volume.size) + 'GiB',
            volume.encrypted and 'encrypted' or 'unencrypted')))
    return

@volumes.command('create_snapshot')
@click.option("--project",default=None, help=" create snapshots for all the volumes based on project")
def create_snapshots(project):
    "Create snapshots for allwait_until_stopped(); the volumes in the instances"
    instances=filter_list(project)
    for data in instances:
        data.stop();
        print("Waiting untill the instance {0} is stopped".format(data.id))
        data.wait_until_stopped();
        for volume in data.volumes.all():
            if has_pending_status(volume):
                print("This volume {0} already has pending status snapshot".format(volume.id))
                continue
            print("Snapshot is created for the instance {0} voulume {1}".format(data.id,volume.id))
            volume.create_snapshot(Description="Created by snapshot analyzer")
            data.start();
            print("Waiting untill the instance {0} is started".format(data.id))
            data.wait_until_running();
    print("All snapshots created!")
    return

@cli.group()
def instances():
    "Group all the instances command"

@instances.command('list')
@click.option("--project", default=None, help="List all the instances based on project")
def list_instances(project):
    "List all the Ec2 instances"
    instances=filter_list(project)
    for data in instances:
        #Replacing this tag  [{'Key': 'project', 'Value': 'snapshots-myproject'}] like
        #{'project':snapshots-myproject'}
        tags={t['Key']:t['Value'] for t in data.tags or []}
        print(",".join((
            data.id,
            data.instance_type,
            data.placement['AvailabilityZone'],
            data.state['Name'],
            data.public_dns_name,
            tags.get('project','No project'))))
    return

@instances.command('stop')
@click.option("--project", default=None, help="stop all the instances based on project")
def stop_instances(project):
    "Stop all the Ec2 instances for a specific project"
    instances=filter_list(project)
    for data in instances:
        print('Stopping the instance of {}'.format(data.id))
        try:
            data.stop()
        except botocore.exceptions.ClientError as exception:
            print("Could not stop the instance {0} getting ".format(exception) + str(exception))
            continue

    return

@instances.command('start')
@click.option("--project", default=None, help="start all the instances based on project")
def start_instances(project):
    "Start all the Ec2 instances for a specific project"
    instances=filter_list(project)
    for data in instances:
        print('Starting the instance of {}'.format(data.id))
        try:
            data.start()
        except botocore.exceptions.ClientError as exception:
            print("Could not start the instance {0} getting ".format(exception)+str(exception))
            continue

    return

if __name__ == '__main__':
     cli()
