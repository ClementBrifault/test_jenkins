node{
    // stage('Git Clone'){
    //     git branch: 'main', credentialsId: 'd08c9709-01cf-417c-a446-57fcb46789a4', url: 'https://github.com/ClementBrifault/test_jenkins'
    // }
    stage('create virtualenv'){
        bat '''python -m venv ..\\virtualenv
        ..\\virtualenv\\Scripts\\pip.exe install -r requirements.txt'''
    }
    stage('run script'){
        bat '..\\virtualenv\\Scripts\\python.exe main.py'
    }
}