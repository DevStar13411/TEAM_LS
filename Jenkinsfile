pipeline {
    agent any
    
    environment {
        GIT_URL = "https://github.com/CodeButter96/TEAM_LS.git"
    }
        
    stages {
        stage('Pull') {
            steps {
                git url: "${GIT_URL}", 
                    branch: "main", 
                    poll: true, 
                    changelog: true,
                    credentialsId: 'github_access_token'
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
                sh 'docker ps -a -q --filter name=mynginx | grep -q . && docker stop mynginx && docker rm mynginx'
                sh 'docker ps -a -q --filter name=gunflask | grep -q . && docker stop gunflask && docker rm gunflask'
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