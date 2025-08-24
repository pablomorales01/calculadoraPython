pipeline {
    agent any

    // 1. ELIMINAMOS el bloque 'environment' que causaba el problema de inyección
    //    ya que 'withSonarQubeEnv' maneja el token automáticamente.

    stages {
    
        stage('Checkout') {
            steps {
                git branch: 'main',
                   url: 'https://github.com/pablomorales01/calculadoraPython.git' // [cite: 3]
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
                    python -m junitxml --output test-results.xml // [cite: 7]
            
                    # 3. Genera el informe de cobertura (Cobertura XML)
                    coverage xml -o coverage.xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // 2. 'withSonarQubeEnv' (con el nombre de tu servidor: 'SonarQube') 
                //    inyecta el token automáticamente como $SONAR_AUTH_TOKEN.
                withSonarQubeEnv('SonarQube') { // 
                    bat '''
                        venv/Scripts/activate
              
                        // 3. USAMOS $SONAR_AUTH_TOKEN (creada por 'withSonarQubeEnv')
                        sonar-scanner -Dsonar.login=%SONAR_AUTH_TOKEN% ^
                          -Dsonar.python.coverage.reportPaths=coverage.xml ^
                          -Dsonar.python.xunit.reportPaths=test-results.xml
                  '''
                }
            }
        }

        stage('Quality Gate') { 
            steps {
                // Espera el resultado del análisis de SonarQube
                waitForQualityGate abortPipeline: true // [cite: 11]
            }
        } 

    } // Cierre del bloque 'stages'

} // Cierre del bloque 'pipeline'