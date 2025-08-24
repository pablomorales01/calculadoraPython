pipeline {
    agent any

    tools {
        // Usa la herramienta SonarQube Scanner que configuraste en Jenkins.
        // El nombre debe coincidir con el que pusiste: 'SonarQube'
        sonarScanner 'SonarQube' 
    }

    environment {
        // Asegúrate de que esta ruta sea la correcta en tu sistema
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
                    REM Crea el entorno virtual
                    %PYTHON_EXE% -m venv venv
               
                    REM Activación del entorno virtual
                    call venv\\Scripts\\activate.bat
                    
                    REM Instalamos las dependencias necesarias
                    %PYTHON_EXE% -m pip install --upgrade pip
                    pip install coverage unittest-xml-reporting
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    REM REACTIVACIÓN en cada nuevo bloque bat
                    call venv\\Scripts\\activate.bat 
            
                    REM 1. Ejecuta las pruebas y genera el XML directamente
                    python -m xmlrunner --output-file test-results.xml

                    REM 2. Ejecuta las pruebas nuevamente para la cobertura y genera el XML
                    coverage run -m unittest discover 
                    coverage xml -o coverage.xml
                '''
            }
        }
        
        stage('Publish Test Results') {
            steps {
                // Publica los resultados de las pruebas
                junit 'test-results.xml' 
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // Inyecta el token de forma segura usando el ID 'sonar-token' que ya configuraste
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    
                    // El bloque withSonarQubeEnv inyecta el PATH del scanner
                    withSonarQubeEnv('SonarQube') {
                        bat '''
                            REM Reactivamos venv y ejecutamos sonar-scanner
                            call venv\\Scripts\\activate.bat && sonar-scanner -Dsonar.login=%SONAR_TOKEN% ^
                              -Dsonar.projectKey=calculadora-python ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.python.xunit.reportPaths=test-results.xml
                        '''
                    }
                }
            }
        }

        stage('Quality Gate') { 
            steps {
                // Espera el resultado del análisis de SonarQube
                waitForQualityGate abortPipeline: true 
            }
        } 
    }
}