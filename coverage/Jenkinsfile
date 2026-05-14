pipeline{
    agent any
    stages{
        stage("checkout"){
            steps{
                echo "========executing checkout========"
                checkout scm
            }
        }            
        stage("setup environment"){
            steps{
                  echo "========executing settingup environment========"
                bat '''
                python -m venv .venv1
                call .venv1\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }
        stage("run tests"){
            steps{
                bat '''
                echo "========executing unittests========"
                call .venv1\\Scripts\\activate
                pytest tests/
                '''
            }
        }
        stage("Deploy"){
            steps{
                bat '''
                 echo "========deploying========"
                 start /B python app.py   
                '''
            }
        }
    }
}    