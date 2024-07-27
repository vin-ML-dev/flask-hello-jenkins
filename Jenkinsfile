pipeline {
 
    agent any
    
    environment {
         CONTAINER_NAME = "my-model"
    }
     
    stages {
        
          
               
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
