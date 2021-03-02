from services.homepagetester.financialreporttester import FinancialReportsTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import InterUnitId

class InterUnitTester(ReconciliationsTester):
    name = "Inter Unit"
            
    
    @bool_logger
    def test_InterUnit(self):
        self.load_url(BASE_URL + URL.interunit)
        self.test_url(URL.interunit)
        self.internal_test(InterUnitId.apar_reco , "apar reco")
        self.internal_test(InterUnitId.mis_sale , "mis sale")
        self.internal_test(InterUnitId.mis_sale_working , "mis sale working")
        self.internal_test(InterUnitId.iut_invoice , "iut invoice")
        self.internal_test(InterUnitId.iut_reco , "iut reco")
    
    def test_Interunit_filter1(self): #yearly #2018-2019 #select all entities #group by entities 

        a = self.get_filter_values_and_id(InterUnitId.frequency)
        list1=[]
        for i in range(len(a)):
            list1.append(a[i]['id'])
        self.find_element(list1[1],'id').click()


        b = self.get_filter_values_and_id(InterUnitId.year)
        list2=[]
        for i in range(len(b)):
            list2.append(b[i]['id'])
        self.find_element(list2[1],'id').click()
        self.find_element(list2[2],'id').click()
        
        
        c = self.get_filter_values_and_id(InterUnitId.quarter)
        list2=[]
        for i in range(len(c)):
            list2.append(c[i]['id'])
        self.find_element(list2[4],'id').click()
        
        self.find_element(InterUnitId.apply).click()
        self.internal_test(InterUnitId.apar_reco , "APAR_RECO Filter check")
        self.internal_test(InterUnitId.mis_sale, "MIS SALE Filter check")
        self.internal_test(InterUnitId.mis_sale_working , "mis_sale_working Filter check")
        self.internal_test(InterUnitId.iut_invoice, "IUT invoice Filter check")
        self.internal_test(InterUnitId.iut_reco, "IUT reco Filter check")
        
 
    
    def run(self):
        try:
            self.test_InterUnit()
            self.test_Interunit_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False   