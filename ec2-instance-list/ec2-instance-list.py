import boto3
import click

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

#'group' in click will group the commands
@click.group()
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
        print('Stopping the instance {}'.format(data.id))
        data.stop()

    return

@instances.command('start')
@click.option("--project", default=None, help="start all the instances based on project")
def start_instances(project):
    "Start all the Ec2 instances for a specific project"
    instances=filter_list(project)
    for data in instances:
        print('Start all the instance {}'.format(data.id))
        data.start()

    return

if __name__ == '__main__':
     instances()
