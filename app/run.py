from services.login.test import LoginTester

def run_app():
    login_test = LoginTester()
    login_test.run()

if __name__=="__main__":
    run_app()

    