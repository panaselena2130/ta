from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePages:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()
        
        
    def do_current_url(self,driver):
       g = driver.current_url

       return g
