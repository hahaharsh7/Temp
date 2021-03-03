import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.services.login.test import LoginTester

def run_app():
    login_test = LoginTester()
    login_test.run()

if __name__=="__main__":
    run_app()

    