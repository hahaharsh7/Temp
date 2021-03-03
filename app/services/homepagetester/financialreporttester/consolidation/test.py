from app.services.homepagetester.financialreporttester.test import FinancialReportsTester
from app.logger.bool_logger import bool_logger
from app.constants import BASE_URL
from app.services.urls import URL
import time
from .id import  ConsolidationId

class ConsolidationReportTester(FinancialReportsTester):
    name = "Consolidation"

    def __init__(self, driver=None):
        if driver:
            self.set_driver(driver)

    @bool_logger
    def test_consolidation(self):
        self.load_url(BASE_URL + URL.consolidation)
        self.test_url(URL.consolidation)
        self.internal_test(ConsolidationId.PL , "PL")
        self.internal_test(ConsolidationId.soce , "soce")
        self.internal_test(ConsolidationId.s_3_12 , "s_3_12")
        
    def test_consolidation_filter1(self): #yearly #2018-2019 #select all entities #group by entities 

        a = self.get_filter_values_and_id(ConsolidationId.freq)
        list1=[]
        for i in range(len(a)):
            list1.append(a[i]['id'])
        self.find_element(list1[2],'id').click()


        b = self.get_filter_values_and_id(ConsolidationId.year)
        list2=[]
        for i in range(len(b)):
            list2.append(b[i]['id'])
        self.find_element(list2[1],'id').click()
        self.find_element(list2[2],'id').click()
        
        
        c = self.get_filter_values_and_id(ConsolidationId.month)
        list2=[]
        for i in range(len(c)):
            list2.append(c[i]['id'])
        self.find_element(list2[4],'id').click()
        self.find_element(list2[5],'id').click()
        
        
        self.find_element(ConsolidationId.apply).click()
        self.internal_test(ConsolidationId.PL , "PL Filter check")
        self.internal_test(ConsolidationId.soce , "SOCE Filter check")
        self.internal_test(ConsolidationId.s_3_12 , "S_3_12 Filter check")
        
 
    
    def run(self):
        try:
            self.test_consolidation()
            self.test_consolidation_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False