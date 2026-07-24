pipeline {
    agent any

    stages {

        stage('Create Sample Project') {
            steps {
                sh '''
                rm -rf sonar-demo
                mkdir sonar-demo
                cd sonar-demo

                cat > app.py << EOF
def add(a, b):
    return a + b

print(add(10,20))
EOF

                cat > sonar-project.properties << EOF
sonar.projectKey=sonar-demo
sonar.projectName=Sonar Demo
sonar.sources=.
sonar.sourceEncoding=UTF-8
EOF
                '''
            }
        }

        stage('Run SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        sh """
                        cd sonar-demo
                        ${scannerHome}/bin/sonar-scanner
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
