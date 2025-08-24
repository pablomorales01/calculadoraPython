pipeline {
    agent any

    tools {
        python 'Python3'                 // Python configurado en Jenkins (Global Tool Configuration)
        sonarQubeScanner 'SonarScanner'  // SonarScanner configurado en Jenkins
    }

    environment {
        SONARQUBE_ENV = credentials('sonar-token') // Token de SonarQube configurado como credencial en Jenkins
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
                    python3 -m venv venv
                    source venv\Scripts\activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    source venv\Scripts\activate
                    # Ejecuta tests si existen, no falla si no hay
                    python -m unittest discover || echo "No tests encontrados"
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat '''
                        source venv\Scripts\activate
                        sonar-scanner -Dsonar.login=$SONARQUBE_ENV
                    '''
                }
            }
        }

        stage('Qua
