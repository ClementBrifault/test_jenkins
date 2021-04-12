node("linux_machine"){
    stage('Git Clone'){
        git branch: 'main', url: 'https://github.com/ClementBrifault/test_jenkins.git'
    }
    stage('create virtualenv'){
        sh '''python3 -m venv ../virtualenv
        ../virtualenv/Scripts/pip install -r requirements.txt'''
    }
    stage('run script'){
        sh '../virtualenv/Scripts/python.exe main.py'
    }
}
