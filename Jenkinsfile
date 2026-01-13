pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/gurudevsinghsandhu/DjangoFoodApp.git' 
        BRANCH = 'gurudev'  
    }

    stages {
        stage('Code Clonning') {
            steps {
                echo 'Cloning code from repository...'
                git url: "${REPO_URL}", branch: "${BRANCH}"
            }
        }

        stage('Building Docker container') {
            steps {
                echo 'Building Docker container...'
                script {
                    def imageTag = "foodapp:${sh(script: 'date +%Y%m%d%H%M%S', returnStdout: true).trim()}"
                    sh "docker build -t ${imageTag} ."
                    env.IMAGE_TAG = imageTag
                }
            }
        }

        stage('Pushing image into Docker repository') {
            steps {
                echo 'Pushing Docker image to repository...'
                script {
                    sh "docker push ${env.IMAGE_TAG}"
                }
            }
        }
        stage('Changing images in deployment file') {
            steps {
                echo 'Updating image in deployment file...'
                sh '''
                sed -i 's|image: my-image:.*|image: my-image:latest|' deployment.yaml
                '''
            }
        }
    }
}
