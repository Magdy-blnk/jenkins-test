def dummy_function():
    """
    A dummy function that does nothing.
    """
    pass



    pipeline {
    agent any
    
    triggers {
        githubPush()  // Use the built-in GitHub webhook trigger
    }
    
    environment {
        REPO_NAME = ''  // Stores the repository name
        DOCKER_IMAGE_NAME = "my-app" // Docker image name
    }
    
    stages {
        stage('Detect Repository') {
            steps {
                script {
                    // Print all environment variables to debug
                    echo "Environment variables:"
                    sh 'env | sort'
                    
                    // Try to determine which repository triggered the build
                    def gitCommit = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    def gitRemote = sh(script: 'git remote -v', returnStdout: true).trim()
                    
                    echo "Git commit: ${gitCommit}"
                    echo "Git remote: ${gitRemote}"
                    
                    // Check which repository contains this commit
                    if (gitRemote.contains("jenkins-test-2.git")) {
                        REPO_NAME = "jenkins-test-2"
                    } 
                    else if (gitRemote.contains("jenkins-test.git")) {
                        REPO_NAME = "jenkins-test"
                    }
                    else if (gitRemote.contains("blnk-crm.git")) {
                        REPO_NAME = "blnk-crm"
                    } else {
                        REPO_NAME = "Unknown"
                        echo "Unknown repository"
                    }
                    
                    echo "Working with repository: ${REPO_NAME}"
                }
            }
        }
        
        stage('Checkout Specific Repository') {
            steps {
                script {
                    // Use SCM checkout for the triggering repository
                    if (REPO_NAME == "jenkins-test") {
                        echo "Checking out jenkins-test repository"
                        checkout([$class: 'GitSCM', 
                            branches: [[name: '*/main']], 
                            userRemoteConfigs: [[credentialsId: '264319f9-2535-4fb1-b553-d751db7d0658', 
                                                url: 'https://github.com/Magdy-blnk/jenkins-test.git']]])
                    } 
                    else if (REPO_NAME == "jenkins-test-2") {
                        echo "Checking out jenkins-test2 repository"
                        checkout([$class: 'GitSCM', 
                            branches: [[name: '*/main']], 
                            userRemoteConfigs: [[credentialsId: '264319f9-2535-4fb1-b553-d751db7d0658', 
                                                url: 'https://github.com/Magdy-blnk/jenkins-test2.git']]])
                    }
                    else if (REPO_NAME == "blnk-crm") {
                        echo "Checking out blnk-crm repository"
                        checkout([$class: 'GitSCM', 
                            branches: [[name: '*/main']], 
                            userRemoteConfigs: [[credentialsId: '264319f9-2535-4fb1-b553-d751db7d0658', 
                                                url: 'https://github.com/Magdy-blnk/blnk-crm.git']]])
                    }
                }
            }
        }
        
        // Add your remaining stages here
    }
}