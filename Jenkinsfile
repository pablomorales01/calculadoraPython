pipeline {
    agent any

    // **IMPORTANTE:** Reemplaza esta ruta con la ruta REAL de tu python.exe
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
                    REM Crea el entorno virtual usando la ruta completa
                    %PYTHON_EXE% -m venv venv
               
                    REM Activación del entorno virtual
                    call venv\\Scripts\\activate.bat
                    
                    pip install --upgrade pip
                    pip install coverage
                    pip install junit-xml
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    REM REACTIVACIÓN: El entorno se debe reactivar en cada nuevo bloque 'bat'
                    call venv\\Scripts\\activate.bat 
            
                    REM Ejecuta las pruebas y guarda el archivo .coverage
                    coverage run -m unittest discover 

                    REM Genera el informe de cobertura (Cobertura XML)
                    coverage xml -o coverage.xml
                    
                    REM Genera el informe de resultados de las pruebas (JUnit XML)
                    REM `junit-xml` no tiene un comando de línea de comandos estándar. 
                    REM `coverage xml` ya genera un reporte de cobertura, y el paso `junit` de Jenkins lee el XML de pruebas
                '''
            }
        }
        
        stage('Publish Test Results') {
            steps {
                // Paso estándar de Jenkins para publicar los resultados de las pruebas
                junit 'test-results.xml' 
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { 
                    bat '''
                        REM REACTIVACIÓN para asegurar que sonar-scanner esté en el PATH
                        call venv\\Scripts\\activate.bat
              
                        REM El token se inyecta automáticamente como %SONAR_AUTH_TOKEN%
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