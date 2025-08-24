pipeline {
    agent any

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
                    
                    pip install --upgrade pip
                    pip install coverage
                    pip install xmlrunner  REM Se instala el runner de pruebas para generar XML
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    REM REACTIVACIÓN en cada nuevo bloque bat
                    call venv\\Scripts\\activate.bat 
            
                    REM 1. Ejecuta las pruebas con xmlrunner para generar el reporte
                    REM    Los resultados se guardarán en la carpeta 'test-reports'
                    python -m xmlrunner --output-file test-results.xml

                    REM 2. Ejecuta las pruebas nuevamente para la cobertura y genera el XML
                    coverage run -m unittest discover 
                    coverage xml -o coverage.xml
                '''
            }
        }
        
        stage('Publish Test Results') {
            steps {
                // Ahora el paso 'junit' encontrará el archivo 'test-results.xml'
                junit 'test-results.xml' 
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { 
                    bat '''
                        REM REACTIVACIÓN
                        call venv\\Scripts\\activate.bat
              
                        REM Usa el token de SonarQube
                        sonar-scanner -Dsonar.login=%SONAR_AUTH_TOKEN% ^
                          -Dsonar.projectKey=calculadora-python ^
                          -Dsonar.sources=. ^
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