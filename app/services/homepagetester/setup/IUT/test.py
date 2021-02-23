from services.homepagetester.financialreporttester import FinancialReportsTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import EFX

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
        r = choice(a)
        if search_el != "":
            r = search_el
        self.find_element(EFX.Input).send_keys(r)
        time.sleep(5)
        b = self.get_element()
        if r not in b:
            return False
        time.sleep(1)
    
    def edit(self):
        pass
        
    def add(self):
        pass
        
    def deleting(self):
        pass
    
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
        time.sleep(15)
        self.test_adjustments()
        return {'remarks': remarks, "value": True}
    
    def run(self):
        try:
            self.test_entry_form()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False