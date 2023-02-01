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
                }
            }
        }
        stage('docker build') {
            steps {
                bat 'docker build -t myimage .'
                bat 'docker run myimage'
                bat 'docker login -u pascalhuang -p dckr_pat_RNrDL5pvTHCaa3sgwn7glkQpPak'
                bat 'docker push pascalhuang/jenkins_pipeline'
            }
        }
    }
}
