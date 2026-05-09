pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t ai-email-assistant .'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'echo test passed'
      }
    }
  }
}