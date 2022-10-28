from selenium.webdriver.common.by import  By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from typing import List

class BasePages:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def webelement_by(self, find_by: str) -> dict:
        find_by = find_by.lower()

        locating = {'xpath': By.XPATH,
                    'css': By.CSS_SELECTOR,
                    'class':By.CLASS_NAME}

        return locating[find_by]



    def are_visible(self, find_by: str, locator: str, locator_name=None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.webelement_by(find_by), locator)),
                               locator_name)



    def do_click(self, find_by: str, locator: str, locator_name) -> List[WebElement]:
         return self.wait.until(ec.element_to_be_clickable((self.webelement_by(find_by), locator)),
                                locator_name).click()

    def get_element_title(self):

        expected_title = input('Enter_expected_name_page_title').upper()
        actual_title=self.driver.title
        try:
            assert expected_title in actual_title
            print("Assertion_Test_Pass_Verification_page")

        except Exception as e:
            print('Assertion Test_Pass_Verification_page failed,enter another name_page_title.', format(e))
            raise
        return actual_title



    def get_text_from_webelements(self,elements:List[WebElement])->List[str]:
        return [element.text for element in elements]



    def get_element_by_text(self,elements:List[WebElement],name: str)->WebElement:
        name=name.lower()
        return [element for element in elements if element.text.lower() == name][0]