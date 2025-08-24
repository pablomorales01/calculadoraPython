pipeline {
    agent any

    // El bloque 'tools' fue eliminado para resolver el error 'Invalid tool type'
    // Ya que estas herramientas a menudo se manejan mejor directamente en el PATH.

    environment {
        // Token de SonarQube configurado como credencial en Jenkins
        SONARQUBE_ENV = credentials('sonar-token') 
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
                    REM Usamos barras inclinadas '/' para la ruta para evitar errores de Groovy
                    venv/Scripts/activate
                    pip install --upgrade pip
                    pip install coverage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    venv/Scripts/activate
            
                    # 1. Ejecuta las pruebas con coverage y las guarda en .coverage 
                    coverage run -m unittest discover 

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
                        venv/Scripts/activate
                        sonar-scanner -Dsonar.login=$SONARQUBE_ENV ^
                        -Dsonar.python.coverage.reportPaths=coverage.xml ^  // Ruta del informe de cobertura
                        -Dsonar.python.xunit.reportPaths=test-results.xml // Ruta del informe de pruebas
                  '''
                }
            }
        }

        stage('Quality Gate') { 
            steps {
                // Espera el resultado del análisis de SonarQube
                // (Requiere que SonarQube esté configurado con el Webhook)
                waitForQualityGate abortPipeline: true 
            }
        } 

    } // Cierre del bloque 'stages'

} // Cierre del bloque 'pipeline'