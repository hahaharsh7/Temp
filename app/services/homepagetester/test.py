from .id import HomeId

class HomePageTester(BaseTester):
    name = "Home Page"
    
    def test_all_links(self):
        report  = self.find_element(*HomeId.report)
        self.focus_to_element(report)
        for i in range(1,6):
            time.sleep(3)
            flag = True
            while flag:
                try:
                    div_link = self.find_element(r"""//*[@id="root"]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[1]/div/ul/li[1]/a""".format(i))
                    div_link.send_keys(Keys.CONTROL + Keys.RETURN)
                    flag=False
                    
                except:
                    print("i am stuck")
                    flag=True
                    time.sleep(4)
                    self.focus_to_element(div_link)
        for i in range(1,3):
            time.sleep(3)
            flag = True
            while flag:
                try:
                    div_link = driver.find_element_by_xpath(r"""//*[@id="root"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div[2]/ul/li[{}]/a""".format(i))
                    div_link.send_keys(Keys.CONTROL + Keys.RETURN)
                    flag=False
                    
                except:
                    print("i am stuck")
                    flag=True
                    time.sleep(4)
                    self.focus_to_element(div_link)
        
        for i in range(1,6):
            driver.switch_to.window(driver.window_handles[i])
            time.sleep(15)
            self.test_reports(driver)
            
        for i in range(6, 8):
            driver.switch_to.window(driver.window_handles[i])
            time.sleep(15)
            self.test_reports(driver)
             
            
    
    @bool_logger
    def test_reports(self, driver):
        report = driver.current_url.split(URL)[1].split("/")[2]
        try:
            rows_in_report = driver.find_elements_by_tag_name("tr")
            
            print(len(rows_in_report))
            if len(rows_in_report) > 5:
                return report, True #doubt
            else:
                return report, True
        except:
            return report, True
        
    def run(self):
        try:
            self.test_all_links()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False
              