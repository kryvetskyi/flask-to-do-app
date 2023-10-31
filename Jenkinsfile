pipeline {
    agent any
    stages {
        stage('Delete Workspace before run'){
            steps {
            echo 'Deleting workspace ...'
            deleteDir()
            }
        }
        stage('Checkout'){
            steps {
                git branch: 'main',
                    url: 'https://github.com/kryvetskyi/flask-to-do-app.git'
                sh 'pwd'
                sh 'ls -la'
            }
        }
        stage('Build docker image'){
            steps {
                sh 'docker build -t anatollucky/app:v01 .'
            }
        }
        stage('Push to Dockerhub'){
            steps{
                withDockerRegistry(credentialsId: 'dockerhub-creds', url: 'https://index.docker.io/v1/' ){
                    sh 'docker push anatollucky/app:v01'
                }
            }
        }
        stage('Delete image locally') {
            steps {
               sh 'docker rmi anatollucky/app:v01'
            }
        }
    }
}
