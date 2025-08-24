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
                    pip install coverage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    source venv\Scripts\activate
            
                    # 1. Ejecuta las pruebas con coverage y las guarda en .coverage coverage run -m unittest discover 

                    # 2. Genera el informe de resultados de las pruebas (JUnit XML)
                    python -m junitxml --output test-results.xml
            
                    # 3. Genera el informe de cobertura (Cobertura XML)
                    coverage xml -o coverage.xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat '''
                        source venv\Scripts\activate
                        sonar-scanner -Dsonar.login=$SONARQUBE_ENV ^
                        -Dsonar.python.coverage.reportPaths=coverage.xml ^  // <--- Ruta del informe de cobertura
                        -Dsonar.python.xunit.reportPaths=test-results.xml // <--- Ruta del informe de pruebas
                    '''
                }
            }
        }

        stage('Qua
