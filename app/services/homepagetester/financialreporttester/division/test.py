import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
# from services.homepagetester.financialreporttester import FinancialReportsTester
from app.services.homepagetester.financialreporttester.test import FinancialReportsTester
from app.logger.bool_logger import bool_logger
from app.constants import BASE_URL
from app.services.urls import URL
from app.services.homepagetester.financialreporttester.division.id import DivisionId
from selenium import webdriver
from app.services.login.test import LoginTester
from app.services.login.id import LoginId as id


class DivisionReportTester(FinancialReportsTester):
    name = "Division"

    def __init__(self, driver = None):
        if driver:
            self.set_driver(driver)

    @bool_logger
    def test_divison(self):
        self.load_url(BASE_URL + URL.divison)
        self.test_url(URL.divison)
        self.internal_test(DivisionId.PL, "PL")
        self.internal_test(DivisionId.Notes, "Notes")
        self.internal_test(DivisionId.Str, "str")
        self.internal_test(DivisionId.pel, "pel")

    def test_division_filter1(self):

        a = self.get_filter_values_and_id(DivisionId.business_filter)
        list1 = []
        for i in range(len(a)):
            list1.append(a[i]['id'])
        self.find_element(list1[1], 'id').click()
        self.find_element(list1[5], 'id').click()

        b = self.get_filter_values_and_id(DivisionId.freq_filter)
        list2 = []
        for i in range(len(b)):
            list2.append(b[i]['id'])
        self.find_element(list2[0], 'id').click()

        self.find_element(DivisionId.apply).click()
        self.internal_test(DivisionId.PL, "PL Filter check")
        self.internal_test(DivisionId.Notes, "Notes Filter check")
        self.internal_test(DivisionId.Str, "str filter check")
        self.internal_test(DivisionId.pel, "pel filter check")

    def run(self):
        try:
            self.test_divison()
            self.test_division_filter1()
            return True
        except Exception as e:
            print(f'Exception occured in class {self.__class__} message:- {e}')
            return False

if __name__ == '__main__':
    DivisionReportTester().run()