pipeline {
    agent any

    stages {
        

        stage('build python env') {
            agent {
                docker {
                    image 'python:3.10-alpine'
                    args '-u root:root'
                    reuseNode true
                }
            }
            steps {
                sh 'echo "With docker"'
                sh 'python3 --version'
                sh 'python3 -m pip install -r requirements.txt'
                
            }
        }
        
        stage('run flask app'){
         agent{
           reuseNode true
         
         } 
         steps{
              sh 'python3 app.py'
         }
        }
    }
}
