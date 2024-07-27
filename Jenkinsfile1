pipeline {
 
    agent {
    docker {
          image 'python:3.9.18-slim'
          args '-u root:root'
          reuseNode true
      }    
    }
    
    environment {
         CONTAINER_NAME = "my-model"
    }
     
    stages {
        
          stage('build python env') {
            
            steps {
                sh 'echo "build python env"'
                sh 'python3 --version'
                sh 'python3 -m pip install -r requirements.txt'
                
                
            }
        }
            
           stage('Training stage') {
            steps {
                    sh 'python train.py'
                    echo "model trained"
                }
        }
        
               
        stage('build docker image') {
            
            steps {
               sh "docker build -t flask-iris-app ."
               
                }
        }
        
        stage('Run docker image'){
         steps {
              sh 'docker stop $CONTAINER_NAME || true'
              sh 'docker rm $CONTAINER_NAME || true'
              sh 'docker run -p 5000:5000 --name $CONTAINER_NAME  flask-iris-app'
              
         }
         
        }
    }
}
