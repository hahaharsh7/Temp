import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.services.homepagetester.financialreporttester.division.test import DivisionReportTester
from app.services.homepagetester.financialreporttester.consolidation.test import ConsolidationReportTester
from app.services.login.test import LoginTester
from app.driver.webdriver import WebDriver as driver

if __name__ == '__main__':
    main_driver = driver().get_driver()
    try:
        LoginTester(main_driver).test_login("admin@namasys.co", "SACRD@214")
        DivisionReportTester(main_driver).run()
        ConsolidationReportTester(main_driver).run()
        ConsolidationReportTester(main_driver).run()

    except Exception as e:
        print(e)