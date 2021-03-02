from services.homepagetester.financialreporttester import FinancialReportsTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import StandaloneId


class StandaloneReportTester(FinancialReportsTester):
    name = "standalone"            
    
    @bool_logger
    def test_Standalone(self):
        self.load_url(BASE_URL + URL.standalone)
        self.test_url(URL.standalone)
        self.internal_test(StandaloneId.PL , "PL")
        self.internal_test(StandaloneId.Notes , "Notes")
        self.internal_test(StandaloneId.cfs , "cfs")
        self.internal_test(StandaloneId.soce , "soce")
        self.internal_test(StandaloneId.s_3_12 , "s_3_12")
        self.internal_test(StandaloneId.ppe , "ppe")
        
    def test_standalone_filter1(self): #yearly #2018-2019 #select all entities #group by entities 
        
            a = self.get_filter_values_and_id(StandaloneId.freq_filter)
            list1=[]
            for i in range(len(a)):
                list1.append(a[i]['id'])
            self.find_element(list1[1],'id').click()


            b = self.get_filter_values_and_id(StandaloneId.year_filter)
            list2=[]
            for i in range(len(b)):
                list2.append(b[i]['id'])
            self.find_element(list2[0],'id').click()


            d = self.get_filter_values_and_id(StandaloneId.quarter)
            list4=[]
            for i in range(len(d)):
                list4.append(d[i]['id'])
            self.find_element(list4[2],'id').click()
            self.find_element(list4[3],'id').click()


            self.find_element(StandaloneId.apply).click()
            self.internal_test(StandaloneId.PL , "PL Filter check")
            self.internal_test(StandaloneId.Notes , "Notes Filter check")
            self.internal_test(StandaloneId.cfs , "cfs Filter check")
            self.internal_test(StandaloneId.soce , "soce Filter check")
            self.internal_test(StandaloneId.s_3_12 , "s_3_12 Filter check")
            self.internal_test(StandaloneId.ppe , "ppe Filter check")
 
    
    def run(self):
        try:
            self.test_Standalone()
            self.test_standalone_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False
