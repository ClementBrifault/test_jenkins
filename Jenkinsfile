node("linux_machine"){
    stage('Git Clone'){
        git branch: 'main', credentialsId: 'd08c9709-01cf-417c-a446-57fcb46789a4', url: 'https://github.com/ClementBrifault/test_jenkins'
    }
    stage('create virtualenv'){
        sh '''python3 -m venv ../virtualenv
        ../virtualenv/Scripts/pip install -r requirements.txt'''
    }
    stage('run script'){
        sh '../virtualenv/Scripts/python.exe main.py'
    }
}
