from app.logger.bool_logger import bool_logger
from app.constants import BASE_URL
from app.services.urls import URL
from app.services.homepagetester.test import HomePageTester
import time


class FinancialReportsTester(HomePageTester):
    name  = 'Financial Reports'
    
    @bool_logger
    def test_url(self,route):
        remarks = "URL loading"
        path = self.current_url.split(BASE_URL)[1]
        if path == route:
            return {'remarks': remarks, "value": True}
        else:
            self.screenshot("url_error")
            return {'remarks': remarks,"value": False ,"error_type" : "Logical Error"}
        time.sleep(10)

    def internal_test(self , keys , name):
        try:
            report = ('checking the loading' , name)
            div_link = self.find_element(keys).click()
            time.sleep(10)
            self.test_reports(report)
        except Exception as e:
            print("i am stuck 1")
            print(e)
            time.sleep(4)
            self.screenshot(e)
                
                    
    @bool_logger
    def test_reports(self , report):
        try:
            rows_in_report = self.find_elements("tr","tag_name") # change this 
            if len(rows_in_report) > 5:
                return {"remarks" : "Data in report", "value" : True ,"extra_path": report[1] } 
            else:
                return {"remarks" : "No Data in report", "value" : False ,"error_type" :"500 server error", "extra_path": report[1] } 
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')   
            return {"remarks" : "Link Not Loading", "value" : False ,"error_type" :"Logical Error" } 
     

    def get_filter_values_and_id(self , xpath):
        res = []
        self.find_element(f'{xpath}/div/button[2]').click()
        element = self.find_element(f'{xpath}/input')
        val = element.get_attribute('id')
        i = 0
        while True:
            result = {}
            try:
                element = self.find_element(f'//*[@id="{val}-option-{i}"]/span/span/input')
                result['id'] = f'{val}-option-{i}'
                result['val'] = self.find_element(f'//*[@id="{val}-option-{i}"]').text
                res.append(result)
                i += 1
            except Exception as e:
                print(e)
                break
        return res
        
    def run(self):
        pass
        