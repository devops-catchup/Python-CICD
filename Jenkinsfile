pipeline {
    agent any
    environment {
        AWS_ACCESS_KEY_ID = credentials('accesskey')
        AWS_SECRET_ACCESS_KEY = credentials('secretkey')
        AWS_REGION = 'ap-south-1'
    }

    stages {
        stage('Checkout the Python code from github') {
            steps {
                git 'https://github.com/devops-catchup/Python-CICD.git'
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'pip install boto3 --break-system-packages'
            }
        }
        stage('Run the Python Script'){
            steps{
                // Export AWS credentials and region and then run the python script
                sh '''
                export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
                export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
                export AWS_DEFAULT_REGION=$AWS_REGION
                python3 ec2instanceboto3.py
                '''
            }
        }
    }
    post {
        success {
            echo 'EC2 INSTNACE CREATED SUCCESSFULLY'
        }
        failure {
            echo 'EC2 instnace creation failed'
        }
    }
}
