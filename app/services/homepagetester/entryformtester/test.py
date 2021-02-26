from services.homepagetester.test import HomePageTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
from .id import EFX
import time
from random import randint


class EntryFormTester(HomePageTester):
    name = "Entry Form"
    
    def get_element(self):
        ar = []
        for link in BS(self.page_source()).findAll("tr"):
            for i in link.findAll('td'):
                ar.append(i.text)
        ar = list(filter(lambda x: x != "", ar))
        return ar
    
    def pages(self):
        if self.find_element(EFX.PageN).is_enabled():
            self.find_element(EFX.PageN).click()
        if self.find_element(EFX.PageP).is_enabled():
            self.find_element(EFX.PageP).click()
        if self.find_element(EFX.PageL).is_enabled():
            self.find_element(EFX.PageL).click()
        if self.find_element(EFX.PageF).is_enabled():
            self.find_element(EFX.PageF).click()
            
    def search(self, search_el=""):
        a = self.get_element()
        r = "Rows per page"
        while "Rows per page" in r:
            r = choice(a)
        if search_el != "":
            r = search_el
        self.find_element(EFX.Input).send_keys(r)
        time.sleep(5)
        b = self.get_element()
        if r not in b:
            return False
        time.sleep(1)
    
    def edit(self, flag=True):
        if flag:
            self.find_element(EFX.Edit).click()
        self.find_element(EFX.Desc).click()
        self.find_element(EFX.D_Op).click()
        self.find_element(EFX.Curr).click()
        self.find_element(EFX.Option[:-1] + str(randint(1, 8)) + EFX.Option[-1]).click()
        self.find_element(EFX.Freq).click()
        f = randint(1, 3)
        self.find_element(EFX.Option[:-1] + str(f) + EFX.Option[-1]).click()
        self.find_element(EFX.Year).click()
        self.find_element(EFX.Option[:-1] + str(randint(1, 3)) + EFX.Option[-1]).click()
        if f == 1:
            self.find_element(EFX.Month).click()
            self.find_element(EFX.Option[:-1] + str(randint(1, 12)) + EFX.Option[-1]).click()
        if f == 2:
            self.find_element(EFX.Quarter).click()
            self.find_element(EFX.Option[:-1] + str(randint(1, 4)) + EFX.Option[-1]).click()
        self.find_element(EFX.Edit).click()
        time.sleep(3)
        
    def add(self):
        self.find_element(EFX.Add).click()
        self.edit(False)
        
    def deleting(self):
        c = EFX.Del[:-22] + str(randint(1, 10)) + EFX.Del[-21:]
        self.find_element(c).click()
        self.find_element(c[:-2] + str(1) + c[-1]).click()
    
    def test_adjustments(self):
        self.pages()
        self.search()
        self.edit()
        self.add()
        self.deleting()
    
    @bool_logger
    def test_entry_form(self):
        remarks = "Entry Form Test"
        self.load_url(BASE_URL + URL.entry_form)
        time.sleep(6)
        self.test_adjustments()
        return {'remarks': remarks, "value": True}
    
    def run(self):
        try:
            self.test_entry_form()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False