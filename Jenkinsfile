pipeline {
    agent any

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
                    // 1. Usa 'python' en lugar de 'python3' si ese es el nombre del ejecutable en Windows.
                    //    Si 'python' tampoco funciona, usa la ruta completa (ej: C:\\Python\\Python310\\python.exe).
                    python -m venv venv
               
                    // 2. ACTIVACIÓN: Usa la sintaxis correcta de Windows para activar un script de Batch.
                    //    El comando debe ser 'call' para que el proceso no termine inmediatamente.
                    call venv\\Scripts\\activate.bat
                    
                    pip install --upgrade pip
                    pip install coverage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    // 3. REACTIVACIÓN: El entorno se debe reactivar en cada bloque 'bat' o 'sh'.
                    call venv\\Scripts\\activate.bat 
            
                    # 1. Ejecuta las pruebas con coverage
                    coverage run -m unittest discover 

                    # 2. Genera el informe de resultados (JUnit XML)
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
                        // 3. REACTIVACIÓN
                        call venv\\Scripts\\activate.bat
              
                        // 4. Se usa %VARIABLE% en Batch.
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