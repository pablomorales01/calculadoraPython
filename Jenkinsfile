pipeline {
    agent any

    environment {
        PYTHON_EXE = "C:\\Users\\pama\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/pablomorales01/calculadoraPython.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    %PYTHON_EXE% -m venv venv
                    call venv\\Scripts\\activate.bat
                    %PYTHON_EXE% -m pip install --upgrade pip
                    pip install coverage unittest-xml-reporting
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    python -m xmlrunner discover -o test-results
                    coverage run -m unittest discover
                    coverage xml -o coverage.xml
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results/*.xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    withSonarQubeEnv('sonar') {
                        bat '''
                            call venv\\Scripts\\activate.bat
                            sonar-scanner ^
                              -Dsonar.login=%SONAR_TOKEN% ^
                              -Dsonar.projectKey=calculadora-python ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.python.xunit.reportPaths=test-results
                        '''
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
    }
}
