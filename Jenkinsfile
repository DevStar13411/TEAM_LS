pipeline {
    agent any
    
    environment {
        GIT_URL = "https://github.com/CodeButter96/TEAM_LS"
    }
        
    stages {
        stage('Pull') {
            steps {
                git url: "${GIT_URL}", branch: "master", poll: true, changelog: true
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t gunflask ./flask/'
                sh 'docker build -t mynginx ./nginx/'
            }
        }
        
        stage('Deploy') {
            steps{
                sh 'docker ps -q --filter name=mynginx | grep -q . && docker stop mynginx && docker rm mynginx'
                sh 'docker ps -q --filter name=gunflask | grep -q . && docker stop gunflask && docker rm gunflask'
                sh 'docker run -d --network="nginx_network" --name gunflask gunflask'
                sh 'docker run -d --network="nginx_network" -p 80:80 --name mynginx mynginx'
            }
        }
        
        stage('Finish') {
            steps{
                sh 'docker images -qf dangling=true | xargs -I{} docker rmi {}'
            }
        }
    }
}