pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.58.0-noble'
            args '--user root'
        }
    }

    environment {
        PYTHONPATH = "${WORKSPACE}"
        HOME = "${WORKSPACE}"
        PLAYWRIGHT_BROWSERS_PATH = "${WORKSPACE}/pw-browsers"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup & Install Dependencies') {
            steps {
                sh '''
                    python -m venv venv
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
            junit testResults: 'test-results.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            cleanWs()
        }
        success {
            echo '🎉 Passed All Test'
        }
        failure {
            echo '❌ Test Failed!'
        }
    }
}