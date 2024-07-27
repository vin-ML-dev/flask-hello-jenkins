pipeline {
 
 agent any
    
    environment {
         CONTAINER_NAME = "run-iris-model"
         CONTAINER_NAME_DEPLOY = "deploy-iris-model"
         DOCKER_IMAGE = 'flask-iris-mlops'
    }
     
    stages {
        
          stage('Building python env') {
            steps {
                  sh 'docker build -t python_env -f files/Dockerfile .'
                  
                  sh 'docker run -d -it --name $CONTAINER_NAME python_env'
               }
           }
            
           stage('Training stage') {
            steps {
                    sh 'docker container exec $CONTAINER_NAME python train.py'
                }
        }
        stage('Test stage') {
              steps {
                    echo "This is testing stage "
                    sh 'docker container exec $CONTAINER_NAME python test.py'
                    sh 'docker stop $CONTAINER_NAME'
                    sh 'docker rm -f $CONTAINER_NAME'
                  }
               }
               
        stage('Deploy') {
              steps {
                    echo "this deploy stage"
                    sh 'docker build -t $DOCKER_IMAGE .'
                    sh 'docker stop $CONTAINER_NAME_DEPLOY || true'
                    sh 'docker rm $CONTAINER_NAME_DEPLOY || true'
                    sh 'docker run -p 5000:5000 --name $CONTAINER_NAME_DEPLOY $DOCKER_IMAGE'
                   
                  }
               }
    }
}
