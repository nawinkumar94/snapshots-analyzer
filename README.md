# snapshots-analyzer
To manage the AWS EC2 intstances snapshots

## About
To list all the instances in the ec2

## configure
Configure our aws using profile
  'aws configure --profile shotty'

## Run
  'pipenv run python ec2-instance-list/ec2-instance-list.py list --project=snapshots-myproject'
  'pipenv run python ec2-instance-list/ec2-instance-list.py stop --project=snapshots-myproject'
  'pipenv run python ec2-instance-list/ec2-instance-list.py start --project=snapshots-myproject'
