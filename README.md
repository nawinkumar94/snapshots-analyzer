# snapshots-analyzer
To manage the AWS EC2 intstances snapshots

## About
To list all the instances in the ec2

## configure
Configure our aws using profile
  'aws configure --profile shotty'
  'pipenv run python shotty/shotty.py <main command> <sub command> --project=snapshots-myproject'

## Run
 'snapshots-myproject' is tag value of instances
  'pipenv run python shotty/shotty.py'
  ## To list recent snapshot
  snapshots list --project=snapshots-myproject
  ##To list all the snapshots
   snapshots list --all --project=snapshots-myproject
  ##To list all the volumes
    volumes list --project=snapshots-myproject
  ##To list all the snapshots
    instances list --project=snapshots-myproject
  ##To create snapshots for all the volumes
    volumes create_snapshot --project=snapshots-myproject
  ##To stop all the intstances
    instances stop --project=snapshots-myproject
  ##To start all the intstances
    instances start --project=snapshots-myproject

## Packaging
   Generating wheel command for packaging
   'pipenv run python setup.py bdist_wheel'
   'pip3 install dist/snapshots_analyzer-0.1-py3-none-any.whl'
