from setuptools import setup

setup(
     name='snapshots-analyzer',
     version='0.1',
     author='NaveenKumar',
     author_email='nawinkumar@gmail.com',
     description='Snapshot analyzer is a tool to manage Aws Ec2 snapshots',
     license="GPLv3+",
     packages=['shotty'],
     url="https://github.com/nawinkumar94/snapshots-analyzer",
     install_requires=[
         'click',
         'boto3'
     ],
     entry_points='''
         [console_scripts]
         shotty=shotty.shotty:cli
     ''',
)
