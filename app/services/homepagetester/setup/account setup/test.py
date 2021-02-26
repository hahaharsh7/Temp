from services.homepagetester.test import HomePageTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
from .id import AccountX
import time
from random import choice


class AccountSetupTester(HomePageTester):
    name = "Account Setup"
    
    def get_element(self):
        ar = []
        for link in BS(self.page_source()).findAll("tr"):
            for i in link.findAll('td'):
                ar.append(i.text)
        ar = list(filter(lambda x: x != "", ar))
        return ar
    
    def pages(self):
        self.find_element(AccountX.PageN).click()
        self.find_element(AccountX.PageP).click()
        self.find_element(AccountX.PageL).click()
        self.find_element(AccountX.PageF).click()
    
    def search(self, search_el=""):
        a = self.get_element()
        r = "Rows per page"
        while "Rows per page" in r:
            r = choice(a)
        if search_el != "":
            r = search_el
        self.find_element(AccountX.Input).send_keys(r)
        time.sleep(5)
        b = self.get_element()
        if r not in b:
            return False
        time.sleep(1)
    
    def edit(self):
        self.find_element(AccountX.Edit).click()
        self.find_element(AccountX.ElC).send_keys("1")
        self.find_element(AccountX.ElD).send_keys(" test")
        self.find_element(AccountX.ElN).click()
        self.find_element(AccountX.ElN).send_keys(Keys.DOWN * 2, Keys.ENTER)
        
    def add(self):
        self.find_element(AccountX.Add).click()
        self.find_element(AccountX.ElC).send_keys("1020")
        self.find_element(AccountX.ElD).send_keys("test_GL_desc")
        self.find_element(AccountX.ElH).click()
        self.find_element(AccountX.ElH).send_keys(Keys.DOWN * 614, Keys.ENTER)
        self.find_element(AccountX.ElS).click()
        self.find_element(AccountX.ElS).send_keys(Keys.DOWN * 5, Keys.ENTER)
        self.find_element(AccountX.ElN).click()
        self.find_element(AccountX.ElN).send_keys(Keys.DOWN * 2, Keys.ENTER)
        self.find_element(AccountX.ElF).send_keys("01-01-0001")
        self.find_element(AccountX.ElT).send_keys("15-02-2021")
        self.find_element(AccountX.ElY).click()
        
    def deleting(self):
        self.find_element(AccountX.Clear).click()
        time.sleep(1)
        self.search("test_GL_desc")
        self.find_element(AccountX.ElW).click()
        time.sleep(1)
        self.find_element(AccountX.ElY).click()
        time.sleep(2)
        if self.get_element()[0] != "No records to display":
            return False
    
    def test_chart_of_accounts(self):
        self.pages()
        self.search()
        self.edit()
        self.add()
        self.deleting()
    
    @bool_logger
    def test_account_setup(self):
        remarks = "Account Setup Test"
        self.load_url(BASE_URL + URL.account_setup)
        time.sleep(15)
        self.test_chart_of_accounts()
        return {'remarks': remarks, "value": True}
    
    def run(self):
        try:
            self.test_account_setup()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False