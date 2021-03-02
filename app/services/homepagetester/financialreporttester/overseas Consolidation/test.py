from services.homepagetester.financialreporttester import FinancialReportsTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import OverseasId

class OverseasReportTester(FinancialReportsTester):
    name = "Overseas Consolidation"
    
    @bool_logger
    def test_overseas(self):
        self.load_url(BASE_URL + URL.overseas_consolidation)
        self.test_url(URL.overseas_consolidation)
        self.internal_test(SubsidiaryId.PL , "PL")
        self.internal_test(SubsidiaryId.Notes , "Notes")
        
    
    def test_overseas_filter1(self): #yearly #2018-2019 #select all entities #group by entities 
        
        a = self.get_filter_values_and_id(OverseasId.freq)
        list1=[]
        for i in range(len(a)):
            list1.append(a[i]['id'])
        self.find_element(list1[1],'id').click()


        b = self.get_filter_values_and_id(OverseasId.quarter)
        list2=[]
        for i in range(len(b)):
            list2.append(b[i]['id'])
        self.find_element(list2[1],'id').click()
        self.find_element(list2[2],'id').click()
        
        
        c = self.get_filter_values_and_id(OverseasId.group)
        list2=[]
        for i in range(len(c)):
            list2.append(c[i]['id'])
        self.find_element(list2[1],'id').click()
        
        
        d = self.get_filter_values_and_id(OverseasId.year)
        list2=[]
        for i in range(len(d)):
            list2.append(d[i]['id'])
        self.find_element(list2[2],'id').click()
        self.find_element(list2[2],'id').click()
        
        
        e = self.get_filter_values_and_id(OverseasId.currency)
        list2=[]
        for i in range(len(e)):
            list2.append(e[i]['id'])
        self.find_element(list2[2],'id').click()
        
        self.find_element(OverseasId.apply).click()
        self.internal_test(OverseasId.PL , "PL Filter check")
        self.internal_test(OverseasId.Notes , "Notes Filter check")
        
        
    
    def run(self):
        try:
            self.test_overseas()
            self.test_overseas_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False
        