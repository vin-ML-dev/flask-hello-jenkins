pipeline {
    agent any

    stages {
        stage('w/o docker') {
            steps {
                sh 'echo "Without docker"'
            }
        }

        stage('w/ docker') {
            agent {
                docker {
                    image 'python:3.10-alpine'
                    args '-u root:root'
                }
            }
            steps {
                sh 'echo "With docker"'
                sh 'python --version'
                sh 'pip3 install flask'
                echo "flask installed"
            }
        }
    }
}
