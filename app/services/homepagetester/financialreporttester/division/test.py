class DivisionReportTester(FinancialReportsTester):
    name = "Division"
    
    @bool_logger
    def test_divison(self):
        self.load_url(BASE_URL + URL.divison)
        self.test_url(URL.divison)
        self.internal_test(DivisionId.PL , "PL")
        self.internal_test(DivisionId.Notes , "Notes")

        
    def test_division_filter1(self):  
        try:
            a = self.get_filter_values_and_id(DivisionId.business_filter)
            list1=[]
            for i in range(len(a)):
                list1.append(a[i]['id'])
            self.find_element(list1[1],'id').click()
            self.find_element(list1[5],'id').click()
            
            
            b = self.get_filter_values_and_id(DivisionId.freq_filter)
            list2=[]
            for i in range(len(b)):
                list2.append(b[i]['id'])
            self.find_element(list2[0],'id').click()
            
            
            d = self.get_filter_values_and_id(DivisionId.groupby)
            list4=[]
            for i in range(len(d)):
                list4.append(d[i]['id'])
            self.find_element(list4[1],'id').click()
    
            
            c = self.get_filter_values_and_id(DivisionId.year_filter)
            list3=[]
            for i in range(len(c)):
                list3.append(c[i]['id'])
            self.find_element(list3[2],'id').click()
            
            self.find_element(DivisionId.apply).click()
            self.internal_test(DivisionId.PL , "PL Filter check")
            self.internal_test(DivisionId.Notes , "Notes Filter check")
            
        except Exception as e:
            print(e)
    
    def run(self):
        try:
            self.test_divison()
            self.test_division_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False