pipeline{
    agent any
    stages{
        stage('Test'){
            steps{
                bat 'pip install -r requirements.txt'
                bat 'start /B python app.py'
                bat 'ping 127.0.0.1 -n 5>nul'
            }
        }
        stage('Build'){
            steps{
                bat 'docker build -t reg:v3'
            }
        }
        stage('Push'){
            steps{
                bat 'docker login -u shivanij454 -p Logan@2020'
                bat 'docker tag reg:v3 shivanij454/registrationapp:seleniumv3'
                bat 'docker push shivanij454/registration:seleniumvv3'
            }
        }
        stage('Deploy'){
            steps{
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'completed'
        }
        failure{
            echo 'Error'
        }
    }
}