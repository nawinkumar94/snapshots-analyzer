# snapshots-analyzer
To manage the AWS EC2 intstances snapshots

## About
To list all the instances in the ec2

## configure
Configure our aws using profile
  'aws configure --profile shotty'
  'pipenv run python ec2-instance-list/ec2-instance-list.py <main command> <sub command> --project=snapshots-myproject'

## Run
  'pipenv run python ec2-instance-list/ec2-instance-list.py'
  ## To list recent snapshot
  snapshots list --project=snapshots-myproject
  ##To list all the snapshots
   snapshots list --all --project=snapshots-myproject
  ##To list all the volumes
    volumes list --project=snapshots-myproject
  ##To create snapshots for all the volumes
    volumes create_snapshot --project=snapshots-myproject
  ##To stop all the intstances
    instances stop --project=snapshots-myproject
  ##To start all the intstances
    instances start --project=snapshots-myproject
