from services.homepagetester.financialreporttester import FinancialReportsTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import GLrecoId

class GLrecoTester(ReconciliationsTester):
    name = "GL Reco"
    
    @bool_logger
    def test_GLreco(self):
        self.load_url(BASE_URL + URL.gl_reco)
        self.test_url(URL.gl_reco)
        self.internal_test(GLrecoId.IUT_reco , "IUT PUR reco")
        
    def test_GLreco_filter1(self): #yearly #2018-2019 #select all entities #group by entities 

        a = self.get_filter_values_and_id(GLrecoId.frequency)
        list1=[]
        for i in range(len(a)):
            list1.append(a[i]['id'])
        self.find_element(list1[1],'id').click()


        b = self.get_filter_values_and_id(GLrecoId.year)
        list2=[]
        for i in range(len(b)):
            list2.append(b[i]['id'])
        self.find_element(list2[0],'id').click()
        
        
        c = self.get_filter_values_and_id(GLrecoId.business)
        list2=[]
        for i in range(len(c)):
            list2.append(c[i]['id'])
        self.find_element(list2[4],'id').click()
        
        d = self.get_filter_values_and_id(GLrecoId.entities)
        list2=[]
        for i in range(len(d)):
            list2.append(d[i]['id'])
        self.find_element(list2[4],'id').click()
        
        e = self.get_filter_values_and_id(GLrecoId.quarter)
        list2=[]
        for i in range(len(e)):
            list2.append(e[i]['id'])
        self.find_element(list2[4],'id').click()
        
        self.find_element(GLrecoId.apply).click()
        self.internal_test(GLrecoId.IUT_reco , "IUT_RECO Filter check")
        
    def run(self):
        try:
            self.test_GLreco()
            self.test_GLreco_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False      