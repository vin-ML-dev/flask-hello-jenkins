pipeline {
    agent any

    stages {
        

        stage('build python env') {
            agent {
                docker {
                    image 'python:3.10-alpine'
                    args '-u root:root'
                }
            }
            steps {
                sh 'echo "With docker"'
                sh 'python --version'
                sh 'pip install virtualenv'
                
                sh 'virtualenv my_env'
                sh 'pip install -r requirements.txt'
                echo "virtual env created"
            }
        }
        
        stage('run flask app'){
        
         steps{
              sh 'python3 app.py'
         }
        }
    }
}
