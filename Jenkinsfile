pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.58.0-noble'
            args '--user root --group-add $(id -g $(stat -c "%U" /var/run/docker.sock))'
        }
    }

    environment {
        PYTHONPATH = "${WORKSPACE}"
        HOME = "${WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh '''
                    . venv/bin/activate
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
    }
}