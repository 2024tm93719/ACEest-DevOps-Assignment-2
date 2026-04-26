pipeline {
    agent any

    environment {
        IMAGE_NAME = "vikashmahala/aceest-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/2024tm93719/ACEest-DevOps-Assignment-2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                bat 'sonar-scanner'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
                bat 'docker tag %IMAGE_NAME%:%IMAGE_TAG% %IMAGE_NAME%:latest'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
                bat 'docker push %IMAGE_NAME%:latest'
            }
        }
    }

    post {
        success {
            echo 'Assignment 2 Jenkins pipeline completed successfully.'
        }
        failure {
            echo 'Assignment 2 Jenkins pipeline failed.'
        }
    }
}