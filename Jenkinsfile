pipeline {
    agent any

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

        stage('Setup Python & Install Dependencies') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    # 安裝 Playwright 瀏覽器（只裝 chromium 較快）
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
            echo '🎉 Passed all tests'
        }
        failure {
            echo '❌ Tests failed, please check the report'
        }
    }
}