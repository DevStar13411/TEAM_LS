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
                sh 'mkdir -p ./flaskapp'
                withCredentials([file(credentialsId: 'flask_config_file', variable: 'flask_config')]) {
                    sh 'cp \$flask_config ./flaskapp/'
                }
                sh 'docker build -t gunflask ./flaskapp/'
                sh 'rm ./flaskapp/config.py'
                sh 'docker build -t nginxvue .'
            }
        }
        
        stage('Deploy') {
            steps{
                sh 'docker ps -a -q --filter name=nginxvue | grep -q . && docker stop nginxvue && docker rm nginxvue'
                sh 'docker ps -a -q --filter name=gunflask | grep -q . && docker stop gunflask && docker rm gunflask'
                sh 'docker run -d --network="nginx_network" --name gunflask gunflask'
                sh 'docker run -d --network="nginx_network" -p 80:80 --name nginxvue nginxvue'
            }
        }
        
        stage('Finish') {
            steps{
                sh 'docker images -qf dangling=true | xargs -I{} docker rmi {}'
            }
        }

        
    }
    post {
        success {
            slackSend (channel: '#젠킨스', color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        failure {
            //slackSend (channel: '#젠킨스', color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
    }
}