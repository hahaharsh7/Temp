from services.homepagetester.financialreporttester import FinancialReportsTester
from logger.bool_logger import bool_logger
from constants import BASE_URL
from services.urls import URL
import time
from .id import SubsidiaryId

class SubsidiaryReportTester(FinancialReportsTester):
    name = "Subsidiary"
   
    @bool_logger
    def test_Subsidiary(self):
        self.load_url(BASE_URL + URL.subsidiary)
        self.test_url(URL.subsidiary)
        self.internal_test(SubsidiaryId.PL , "PL")
        self.internal_test(SubsidiaryId.Notes , "Notes")
        
    def test_subsidary_filter1(self): #yearly #2018-2019 #select all entities #group by entities 
        
            a = self.get_filter_values_and_id(SubsidiaryId.freq_filter) #selects monthly in the frequqncy
            list1=[]
            for i in range(len(a)):
                list1.append(a[i]['id'])
            self.find_element(list1[2],'id').click()


            b = self.get_filter_values_and_id(SubsidiaryId.year_filter) #year filyer , check 1 and 2 
            list2=[]
            for i in range(len(b)):
                list2.append(b[i]['id'])
            self.find_element(list2[1],'id').click()
            self.find_element(list2[2],'id').click()


#             d = self.get_filter_values_and_id(SubsidiaryId.location)    enable when location is funcational
#             list4=[]
#             for i in range(len(d)):
#                 list4.append(d[i]['id'])
#             self.find_element(list4[2],'id').click()
#             self.find_element(list4[3],'id').click()
            c = self.get_filter_values_and_id(SubsidiaryId.business) #trading and holography in businesses
            list2=[]
            for i in range(len(c)):
                list2.append(c[i]['id'])
            self.find_element(list2[3],'id').click()
            self.find_element(list2[4],'id').click()
            
            d = self.get_filter_values_and_id(SubsidiaryId.entities) #select all entities
            list2=[]
            for i in range(len(d)):
                list2.append(d[i]['id'])
            self.find_element(list2[0],'id').click()
           
            e = self.get_filter_values_and_id(SubsidiaryId.currency) #INR currency
            list2=[]
            for i in range(len(e)):
                list2.append(e[i]['id'])
            self.find_element(list2[1],'id').click()
            
            f = self.get_filter_values_and_id(SubsidiaryId.month) #year filyer , check 1 and 2 
            list2=[]
            for i in range(len(f)):
                list2.append(f[i]['id'])
            self.find_element(list2[1],'id').click()
            self.find_element(list2[2],'id').click()
            self.find_element(list2[3],'id').click()



            self.find_element(SubsidiaryId.apply).click()
            self.internal_test(SubsidiaryId.PL , "PL Filter check")
            self.internal_test(SubsidiaryId.Notes , "Notes Filter check")
 
    
    def run(self):
        try:
            self.test_Subsidiary()
            self.test_subsidary_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False