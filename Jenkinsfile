pipeline {
    agent any   // 使用 Jenkins 本身容器執行，避免 docker permission 問題

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
                    # 安裝 Python 和必要工具
                    apt-get update -qq
                    apt-get install -y python3 python3-venv python3-pip curl
                    
                    # 建立虛擬環境並安裝依賴
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    # 安裝 Playwright 瀏覽器（只裝 chromium，比較快）
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
            echo '🎉Passed All Tested'
        }
        failure {
            echo '❌ Tests Failed'
        }
    }
}