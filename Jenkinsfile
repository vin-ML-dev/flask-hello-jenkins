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
                sh 'pip install --upgrade pip'
                sh 'pip install venv'
                sh 'python -m venv my_env'
                sh 'source myenv/bin/activate'
                sh 'pip install -r requirements.txt'
                echo "virtual env created"
            }
        }
    }
}
