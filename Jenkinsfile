node("windows"){
    stage('Git Clone'){
        git branch: 'main', url: 'https://github.com/ClementBrifault/test_jenkins.git'
    }
    stage('create virtualenv'){
        bat '''python -m venv ..\\virtualenv
        ..\\virtualenv\\Scripts\\pip install -r requirements.txt'''
    }
    stage('run script'){
        bat '..\\virtualenv\\Scripts\\python.exe main.py'
    }
}
