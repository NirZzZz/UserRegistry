pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'userregistry'
        DATABASE_PASSWORD = credentials('DATABASE_PASSWORD')
        DATABASE_HOST = credentials('HOST')
        DATABASE_PORT = credentials('DATABASE_PORT')
        DATABASE_USER = credentials('DATABASE_USER')
        HOST = credentials('HOST')
        REST_PORT = credentials('REST_PORT')
        WEB_PORT = credentials('WEB_PORT')
        REST_URL = credentials('REST_URL')
        WEB_URL = credentials('WEB_URL')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set up Docker Buildx') {
            steps {
                script {
                    sh 'docker buildx create --use'
                }
            }
        }

        stage('Log in to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DOCKER_CREDENTIALS', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    sh 'pyenv install 3.9 || true'
                    sh 'pyenv global 3.9'
                }
            }
        }

        stage('Install Docker Compose') {
            steps {
                sh '''
                sudo apt-get update
                sudo apt-get install -y docker-compose
                '''
            }
        }

        stage('Create .env file') {
            steps {
                script {
                    sh '''
                    echo DATABASE_PASSWORD="${DATABASE_PASSWORD}" >> .env
                    echo DATABASE_HOST="${DATABASE_HOST}" >> .env
                    echo DATABASE_PORT="${DATABASE_PORT}" >> .env
                    echo DATABASE_USER="${DATABASE_USER}" >> .env
                    echo HOST="${HOST}" >> .env
                    echo REST_PORT="${REST_PORT}" >> .env
                    echo WEB_PORT="${WEB_PORT}" >> .env
                    echo REST_URL="${REST_URL}" >> .env
                    echo WEB_URL="${WEB_URL}" >> .env
                    '''
                }
            }
        }

        stage('Build Docker Containers') {
            steps {
                script {
                    sh '''
                    docker-compose down -v || true
                    docker-compose build
                    docker-compose up -d
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install chromedriver-py
                    '''
                }
            }
        }

        stage('Check Docker Compose Logs') {
            steps {
                script {
                    sh 'docker-compose logs'
                }
            }
        }

        stage('Run Combined Tests') {
            steps {
                script {
                    sh 'PYTHONPATH=. python tests/combined_testing.py'
                }
            }
        }

        stage('Clean up Docker Containers') {
            steps {
                script {
                    sh 'docker-compose down -v'
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DOCKER_CREDENTIALS', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh '''
                        docker tag $DOCKER_IMAGE $DOCKER_USERNAME/$DOCKER_IMAGE:V1
                        docker push $DOCKER_USERNAME/$DOCKER_IMAGE:V1
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
