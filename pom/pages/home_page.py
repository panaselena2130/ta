import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePages

from typing import List, Tuple, Any
from selenium.webdriver.remote.webelement import WebElement

from pom.pages.utils import Utils


class HomePage(BasePages):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver
        self.locator_More_about: str = '//*[@id="mainContent"]/index-lobby/section[1]/div/div/section[2]'
        self.locator_Index_component: str = '//*[@id="more_madad_nav"]/ul/li[1]/ul/li[4]/a'
        self.locator_market_Data: str = '#mainContent > index-lobby > index-composition > index-weight > gridview-lib > div > div.container > div > filter-data > div > div.table_sorting_box > div > div.table_sorting_separator.no_border > div > label:nth-child(4)'
        self.locator_Turn_up_down: str = '#mainContent > index-lobby > index-composition > index-market-data > gridview-lib > div > div.container > div > div > div.table_page_table_container > table > thead > tr.sort-btns > td:nth-child(6) > ul > li:nth-child(2) > button'
        self.locator_Company: str = '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody/tr'
        self.locator_: str = '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody'





    def load_page(self):
        self.driver.get('https://www.tase.co.il/en/market_data/index/137/major_data')


    def list_of_Ind_Homepage(self) -> List[WebElement]:
        return self.are_visible('xpath', self.locator_Company, 'All_index_of_TA-125')

    def text_of_list_Ind_Homepage(self) -> str:

        all = self.list_of_Ind_Homepage()
        d_text=self.get_text_from_webelements(all)
        return Utils.join_strings(d_text)

    def major_data(self):
        self.do_click('xpath',self.locator_More_about,'More_About')
        self.do_click('xpath',self.locator_Index_component,'Index_component')
        self.do_click('css',self.locator_market_Data,'Market_data')
        self.do_click('css',self.locator_Turn_up_down,'Turnover')




    def get_nav_link_by_name(self,name):
        elements = self.list_of_Ind_Homepage()
        print(elements,type(elements),"Webelements")
        return self.get_element_by_text(elements,name)



    



