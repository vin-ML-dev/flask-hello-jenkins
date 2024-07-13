pipeline {
    agent any

    stages {
        

        stage('get-files') {
            agent {
                docker {
                    image 'python:3.10-alpine'
                    args '-u root:root'
                    
                }
            }
            steps {
                cleanWs()
                sh 'echo "With docker"'
                sh 'python --version'
                sh 'pip3 install -r requirements.txt'
                echo "flask installed"
                sh 'python app.py'
            }
        }
    }
}
