from abc import ABC, abstractmethod
from .validator import ValidatorMixin
from driver.webdriver import WebDriver

class BaseTester(WebDriver, ValidatorMixin,ABC):
    """This base class provides basic functionality to helps all testing classes"""
    name = "#SACRD"
    
    @classmethod
    def get_name(cls):
        if cls.__name__ == "BaseTester":
            return BaseTester.name
        else:
            return f'{cls.__bases__[0].get_name()}>>{cls.name}'
        
        
    @abstractmethod
    def run(self):
        pass