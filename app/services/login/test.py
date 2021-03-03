from app.services.basetester import BaseTester
from app.logger.bool_logger import bool_logger
from app.constants import BASE_URL
from app.services.urls import URL
from app.services.login.id import LoginId
import time


class LoginTester(BaseTester):
    name = "Login Page"

    def __init__(self, driver=None):
        if driver:
            self.set_driver(driver)

    @bool_logger
    def test_login(self, email_id, password):
        self.load_url(BASE_URL + URL.login)
        elemLoginId = self.find_element(*LoginId.EMAIL)
        elemLoginId.send_keys(email_id)
        elemLoginPassword = self.find_element(*LoginId.PASSWORD)
        elemLoginPassword.send_keys(password)
        elemLoginCheckBox = self.find_element(*LoginId.AGREEBUTTON)
        elemLoginCheckBox.click()
        elemLoginButton = self.find_element(*LoginId.LOGINSUBMIT)
        elemLoginButton.click()
        time.sleep(5)
        path = self.current_url.split(BASE_URL)[1]
        login_remarks = "Checking Login Flow"
        if path == URL.home:
            return {"remarks": login_remarks, "value": True}
        else:
            self.screenshot(login_remarks)
            return {"remarks": "Home Link Not Loading", "value": False, "error_type": "Logical Error"}

    @bool_logger
    def test_reset_password(self, new_password, confirm_password):
        remarks = "Reset Password Successfully"
        return {"remarks": remarks, "value": False, "error_type": "Logical Error"}

    def run(self):
        try:
            self.test_login("admin@namasys.co", "SACRD@214")
            self.test_reset_password("a", "b")
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False
