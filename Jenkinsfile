pipeline {
    agent any
    stages {
        stage('Testing') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and Push Images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }
        stage('Ansible') {
            steps {
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }

        stage('Deploying') {
            steps {
                sh "scp -i /home/jenkins/.ssh/id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                sh "scp -i /home/jenkins/.ssh/id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
            }
        }
    }
    post {
        always {
            sh "docker logout"
            }
        }
    }
