pipeline {
    agent any

    // 1. **IMPORTANTE:** Reemplaza esta ruta con la ruta REAL donde está instalado python.exe en tu servidor Jenkins.
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
                    pip install junit-xml  REM Se instala el paquete para generar el reporte JUnit
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    REM REACTIVACIÓN: Se debe reactivar el entorno virtual en cada nuevo bloque 'bat'
                    call venv\\Scripts\\activate.bat 
            
                    REM 1. Ejecuta las pruebas y genera el archivo .coverage
                    coverage run -m unittest discover 

                    REM 2. Genera el informe de cobertura (Cobertura XML)
                    coverage xml -o coverage.xml
                    
                    REM 3. Genera el informe de resultados de las pruebas (JUnit XML)
                    REM Nota: Asume que el runner de coverage genera test-results.xml, si no, ajusta el comando aquí.
                    REM Si el comando falla, consulta la documentación de 'junit-xml'
                    
                '''
                // **Nota:** No incluimos el comando 'junitxml' aquí porque a veces el runner de cobertura lo hace
                // o porque es más fácil usar el paso 'junit' de Jenkins. 
            }
        }
        
        stage('Publish Test Results') {
            steps {
                // Paso estándar de Jenkins para publicar los resultados de las pruebas (basado en el XML generado)
                // Ajusta el nombre del archivo si es diferente
                junit 'test-results.xml' 
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // **IMPORTANTE:** El nombre 'SonarQube' DEBE coincidir exactamente con el configurado en Jenkins
                withSonarQubeEnv('SonarQube') { 
                    bat '''
                        REM REACTIVACIÓN para asegurar que sonar-scanner esté en el PATH si fue instalado en el venv
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
                // Espera el resultado del análisis de SonarQube
                waitForQualityGate abortPipeline: true 
            }
        } 
    }
}