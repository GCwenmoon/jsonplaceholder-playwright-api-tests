pipeline {
    agent any   // Use Agent Any

    environment {
        HOME = "${WORKSPACE}"
        PLAYWRIGHT_BROWSERS_PATH = "${WORKSPACE}/pw-browsers"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                sh '''
                    apt-get update -qq
                    apt-get install -y python3 python3-venv python3-pip curl
                    
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    playwright install --with-deps chromium
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    
                    pytest tests/ \
                        --verbose \
                        --html=report.html \
                        --self-contained-html \
                        --junitxml=test-results.xml
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'test-results.xml', 
                  allowEmptyResults: true, 
                  keepLongStdio: true
            
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
        success {
            echo '🎉 Passed all tests'
        }
        failure {
            echo '❌ Build or Test Failed'
        }
    }
}