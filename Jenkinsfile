pipeline {
    agent {
    docker {
          image 'python:3.8-slim'
          args '-u root:root'
          reuseNode true
      }    
    }
    
    environment {
        
        CONTAINER_NAME = "flask-demo-jenkins"
        
    }
       
    

    stages {
    
       stage('Train model') {
            
            steps {
               sh 'python -m pip install -r requirements.txt'
               sh "python train.py"
               echo "model trained"
               
                }
        }
        

        stage('build docker image') {
            
            steps {
                 
                  sh "docker build -t flask-demo-jenkins ."
               
                }
        }
        
        stage('Run docker image'){
         steps {
              sh 'docker stop $CONTAINER_NAME || true'
              sh 'docker rm $CONTAINER_NAME || true'
              sh 'docker run -p 5000:5000 --name $CONTAINER_NAME flask-demo-jenkins'
              
         }
         
        }
        
        
    }
}
