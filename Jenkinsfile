pipeline {
    agent any
       
    

    stages {
        

        stage('build docker image') {
            
            steps {
               sh "docker build -t flask-demo-jenkins ."
               
                }
        }
        
        stage('Run docker image'){
         steps {
              sh 'docker run -p 5000:5000 flask-demo-jenkins'
              
         }
         
        }
        
        
    }
}
