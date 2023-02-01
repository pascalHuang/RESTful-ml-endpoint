pipeline {
    agent any
    stages {
        stage('Say Hello World') {
            steps {
                echo "hello world"
            }
        }
        stage('Build and Test') {
            steps {
                echo 'Building Python application...'
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'python test_main.py'
            }
        }
        stage('Create Staging Branch') {
            steps {
                sshagent(credentials: ['64e1eb8f-67f2-4ad9-aff8-74ea77af2a9a']) {
                sh "git branch --delete staging"
                sh "git branch staging"
                sh "git checkout staging"
                sh "git push origin staging"
		echo 'branch created'
                }
            }
        }
        stage('docker build') {
            steps {
                echo 'Building docker image...'
		bat 'docker build -t monimage .'
		bat 'docker run -d monimage'
            }
        }
    }
}
