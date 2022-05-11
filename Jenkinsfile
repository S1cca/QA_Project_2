pipeline {
    agent any
    stages {
        stage('Testing') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "sudo docker-compose build --parallel"
                sh "sudo docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "sudo docker-compose push"
            }
        }
        // stage('Deploy') {
        //     steps {
        //         sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
        //         sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
        //         sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
        //     }
        // }
    }
    // post {
    //     always {
    //         junit '**/*.xml'
    //         cobertura coberturaReportFile: 'service_1/coverage.xml', failNoReports: false
    //         cobertura coberturaReportFile: 'service_2/coverage.xml', failNoReports: false
    //         cobertura coberturaReportFile: 'service_3/coverage.xml', failNoReports: false
    //         cobertura coberturaReportFile: 'service_4/coverage.xml', failNoReports: false
    //     }
    // }
}