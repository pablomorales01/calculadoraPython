pipeline {
    agent any

    // Define la ruta de Python como una variable de entorno para usarla en todos los bloques 'bat'
    environment {
        // **IMPORTANTE:** Cambia esta ruta por la ruta real donde está instalado python.exe en tu servidor Jenkins.
        PYTHON_EXE = "C:\\Python\\Python310\\python.exe" // Ejemplo
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
                    REM Crea el entorno virtual usando la ruta completa
                    %PYTHON_EXE% -m venv venv
               
                    REM 2. ACTIVACIÓN: Es crucial usar 'call' y la sintaxis de Windows.
                    call venv\\Scripts\\activate.bat
                    
                    pip install --upgrade pip
                    pip install coverage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    REM REACTIVACIÓN: El entorno se debe reactivar en cada bloque 'bat'
                    call venv\\Scripts\\activate.bat 
            
                    REM 1. Ejecuta las pruebas con coverage
                    coverage run -m unittest discover 

                    REM 2. Genera el informe de resultados (JUnit XML)
                    %PYTHON_EXE% -m junitxml --output test-results.xml
            
                    REM 3. Genera el informe de cobertura (Cobertura XML)
                    coverage xml -o coverage.xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat '''
                        REM REACTIVACIÓN
                        call venv\\Scripts\\activate.bat
              
                        REM Usa %SONAR_AUTH_TOKEN% para el login
                        sonar-scanner -Dsonar.login=%SONAR_AUTH_TOKEN% ^
                          -Dsonar.python.coverage.reportPaths=coverage.xml ^
                          -Dsonar.python.xunit.reportPaths=test-results.xml
                  '''
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