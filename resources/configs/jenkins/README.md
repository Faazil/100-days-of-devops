# ⚙️ Jenkins Pipeline Configurations

CI/CD pipeline configurations using Jenkins declarative and scripted pipelines.

## 📁 Available Files

| File | Description | Features |
|------|-------------|----------|
| `jenkins-multistage-pipeline.jenkinsfile` | Multi-stage pipeline | Build, Test, Deploy stages |
| `jenkins-pipeline-deploy-077.jenkinsfile` | Deployment pipeline | Automated deployment |
| `jenkins-pipeline-parameter.jenkinsfile` | Parameterized build | User input parameters |
| `jenkins_httpd_installation_job.jenkinsfile` | Package installation | Server configuration |
| `jenkins_scm_trigger_deployment.jenkinsfile` | SCM-triggered build | Git webhook integration |

---

## 🚀 Quick Start

### Creating a Pipeline Job

1. **In Jenkins UI**:
   - New Item → Pipeline
   - Name your pipeline
   - Select "Pipeline script from SCM"
   - Choose Git and provide repository URL
   - Specify Jenkinsfile path

2. **Run Pipeline**:
   - Click "Build Now"
   - View Console Output
   - Check Blue Ocean view for visual pipeline

---

## 📚 Learning Points

### Declarative Pipeline Structure

```groovy
pipeline {
    agent any

    environment {
        APP_NAME = 'myapp'
        VERSION = '1.0'
    }

    stages {
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker build -t ${APP_NAME}:${VERSION} .'
                sh 'docker push ${APP_NAME}:${VERSION}'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
```

### Common Pipeline Patterns

1. **Parallel Stages**
   ```groovy
   stage('Tests') {
       parallel {
           stage('Unit Tests') {
               steps {
                   sh 'npm run test:unit'
               }
           }
           stage('Integration Tests') {
               steps {
                   sh 'npm run test:integration'
               }
           }
       }
   }
   ```

2. **Conditional Execution**
   ```groovy
   stage('Deploy to Production') {
       when {
           branch 'main'
       }
       steps {
           sh './deploy-prod.sh'
       }
   }
   ```

3. **Parameters**
   ```groovy
   parameters {
       string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Environment')
       choice(name: 'VERSION', choices: ['1.0', '2.0'], description: 'Version')
       booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests?')
   }
   ```

4. **Credentials**
   ```groovy
   environment {
       AWS_CREDENTIALS = credentials('aws-creds')
       DOCKER_HUB = credentials('dockerhub-token')
   }
   ```

---

## 🔧 Advanced Features

### Post-Build Actions

```groovy
post {
    always {
        // Always run
        junit 'reports/**/*.xml'
    }
    success {
        // On success
        slackSend color: 'good', message: "Build succeeded: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
    }
    failure {
        // On failure
        mail to: 'team@example.com',
             subject: "Build Failed: ${env.JOB_NAME}",
             body: "Check: ${env.BUILD_URL}"
    }
    cleanup {
        // Clean workspace
        cleanWs()
    }
}
```

### Docker Integration

```groovy
pipeline {
    agent {
        docker {
            image 'node:14'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
    }
}
```

### Shared Libraries

```groovy
@Library('my-shared-library') _

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    buildApp()  // Custom function from shared library
                }
            }
        }
    }
}
```

---

## 🔒 Best Practices

- ✅ Use declarative syntax over scripted
- ✅ Store credentials in Jenkins Credentials Store
- ✅ Use environment variables for configuration
- ✅ Implement proper error handling
- ✅ Archive artifacts after builds
- ✅ Use Jenkins shared libraries for reusability
- ✅ Implement pipeline linting
- ✅ Use Blue Ocean for better visualization
- ✅ Enable build timeout
- ✅ Clean workspace after builds

### Security

```groovy
// Don't do this
environment {
    PASSWORD = 'hardcoded123'  // ❌ Bad
}

// Do this instead
environment {
    PASSWORD = credentials('db-password')  // ✅ Good
}
```

---

## 🚀 CI/CD Pipeline Example

```groovy
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'myapp'
        REGISTRY = 'docker.io'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run ${DOCKER_IMAGE}:${BUILD_NUMBER} npm test'
            }
        }

        stage('Push') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo ${PASS} | docker login -u ${USER} --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'kubectl set image deployment/myapp myapp=${DOCKER_IMAGE}:${BUILD_NUMBER}'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
```

---

## 📖 Related Challenges

- **Day 68-86**: Jenkins CI/CD (Weeks 11-12)
- Topics: Pipelines, Multi-stage builds, Deployments, SCM integration

---

## 🔗 Additional Resources

- [Jenkins Official Documentation](https://www.jenkins.io/doc/)
- [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Jenkins Blue Ocean](https://www.jenkins.io/projects/blueocean/)
- [Jenkins Shared Libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/)

---

[← Back to Resources](../README.md) | [Main README](../../../README.md)
