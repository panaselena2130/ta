from selenium.webdriver.common.by import  By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from typing import List

class BasePages:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10,0.5)

    def webelement_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'xpath': By.XPATH,
                 'css': By.CSS_SELECTOR,
                 'class':By.CLASS_NAME,
                    'name':By.NAME
                    }

        return locating[find_by]



    def are_visible(self, find_by: str, locator: str, locator_name=None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.webelement_by(find_by), locator)),
                               locator_name)

    def do_click(self, find_by: str, locator: str, locator_name=None) -> List[WebElement]:
        return self.wait.until(ec.element_to_be_clickable((self.webelement_by(find_by), locator)),
                               locator_name).click()




    def get_text_from_webelements(self,elements:List[WebElement])->List[str]:
        element_list = []
        for element in elements:
            element_list.append(element.text)
            print(element_list,'ELEMENT_LIST')

        return element_list



    def get_element_by_text(self,elements:List[WebElement],name: str)->WebElement:
        name=name.lower()


        return [element for element in elements if element.text.lower() == name][0]

