import boto3
import boto3.resources

# create ec2 resource
ec2_resource = boto3.resource('ec2')

# Launch as EC2 Instance
instances = ec2_resource.create_instances(
    ImageId = 'ami-00bb6a80f01f03502',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'ec2-python',

    # ADD the EBS Volume size TO 20GB 
    BlockDeviceMappings = [
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 20,
                'VolumeType': 'gp2',
                'DeleteOnTermination': False
            }
        }
    ],
    # Assign the Tag to Instance
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags': [ 
                {
                    'Key': 'Name',
                    'Value':'MyJenkinsPythonServer',
                },
                {
                    'Key': 'Env',
                    'Value': 'Dev'
                }
            ]
        }
    ],
    # Add UserData for installing some Apache packages while launching instnace
    UserData = '''#!/bin/bash
    # Update the package list
    sudo apt update -y
    # Install Apache
    sudo apt install apache2 -y
    # Start Apache Service
    sudo systemctl start apache2
    # Enable the Apache service
    sudo systemctl enable apache2
    # Create sample index.html file
    echo "<html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>" | sudo tee /var/www/html/index.html
    # Allow Apache from firewall
    sudo ufw allow 'Apache'
    ''',
)
