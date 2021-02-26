from services.homepagetester.test import HomePageTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import IUTX


class IUTSetupTester(HomePageTester):
    name = "IUT Setup"
    
    def get_element(self):
        ar = []
        for link in BS(self.page_source()).findAll("tr"):
            for i in link.findAll('td'):
                ar.append(i.text)
        ar = list(filter(lambda x: x != "", ar))
        return ar
    
    def pages(self):
        if self.find_element(IUTX.PageN).is_enabled():
            self.find_element(IUTX.PageN).click()
        if self.find_element(IUTX.PageP).is_enabled():
            self.find_element(IUTX.PageP).click()
        if self.find_element(IUTX.PageL).is_enabled():
            self.find_element(IUTX.PageL).click()
        if self.find_element(IUTX.PageF).is_enabled():
            self.find_element(IUTX.PageF).click()
            
    def search(self, search_el=""):
        a = self.get_element()
        r = "Rows per page"
        while "Rows per page" in r:
            r = choice(a)
        if search_el != "":
            r = search_el
        self.find_element(IUTX.Input).send_keys(r)
        time.sleep(5)
        b = self.get_element()
        if r not in b:
            return False
        self.find_element(IUTX.Clear).click()
        time.sleep(1)
    
    def edit(self, flag=True):
        for i in range(5):
            self.find_element(IUTX.Edit[:-18] + str(i + 1) + IUTX.Edit[-18:]).click()
            if i != 0 and i != 3:
                self.find_element(IUTX.Gross[:-33] + str(i + 1) + IUTX.Gross[-33:]).click()
                self.find_element(IUTX.SelectAll).click()
            self.find_element(IUTX.Net[:-33] + str(i + 1) + IUTX.Net[-33:]).click()
            self.find_element(IUTX.SelectAll).click()
            self.find_element(IUTX.Edit[:-18] + str(i + 1) + IUTX.Edit[-18:] + "[1]").click()
            time.sleep(4)
            
        self.find_element(IUTX.Reset).click()
    
    def test_gross_net(self):
        self.pages()
        self.search()
        self.edit()
    
    @bool_logger
    def test_iut_setup(self):
        remarks = "IUT Setup Test"
        self.load_url(BASE_URL + URL.iut_setup)
        time.sleep(6)
        self.test_gross_net()
        return {'remarks': remarks, "value": True}
    
    def run(self):
        try:
            self.test_iut_setup()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False