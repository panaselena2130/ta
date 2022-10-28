

import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePages

from typing import List, Tuple, Any
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePages):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver
        self.locator_More_about: str = '//*[@id="mainContent"]/index-lobby/section[1]/div/div/section[2]'
        self.locator_Index_component: str = '//*[@id="more_madad_nav"]/ul/li[1]/ul/li[4]/a'
        self.locator_market_Data: str = '#mainContent > index-lobby > index-composition > index-weight > gridview-lib > div > div.container > div > filter-data > div > div.table_sorting_box > div > div.table_sorting_separator.no_border > div > label:nth-child(4)'
        self.locator_market_Data_1: str = '//*[@id="mainContent"]/index-lobby/index-composition/index-weight/gridview-lib/div/div[2]/div/filter-data/div[1]/div[2]/div/div[1]/div/label[2]'
        self.locator_Turn_up_down: str = '#mainContent > index-lobby > index-composition > index-market-data > gridview-lib > div > div.container > div > div > div.table_page_table_container > table > thead > tr.sort-btns > td:nth-child(6) > ul > li:nth-child(2) > button'
        self.locator_Turn_up_down_2: str = '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/thead/tr[2]/td[6]/ul/li[2]/button'
        self.locator_Turn_up_down_1: str = 'glyphicon glyphicon-menu-down sorting_button selected'
        self.locator_Company: str = '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody/tr'
        self.locator_: str = '/en/market_data/security'
        self.locator_class: str = 'item-name'
        self.locator_1Y: str = '//*[@id="mainContent"]/security-lobby/security-major/section[1]/div/div[1]/div/div[2]/chart-period-menu/ul/li[6]/a'


    def load_page(self):
        self.driver.get('https://www.tase.co.il/en/market_data/index/137/major_data')

    def verific_page(self)->str:
        return self.get_element_title()


    def major_data(self,switch:int):
        match switch:
            case 0:
                return self.do_click('xpath',self.locator_More_about, locator_name='More_About')

            case 1:
                return self.do_click('xpath',self.locator_Index_component,locator_name='Index_component')

            case 2:
                return self.do_click('xpath',self.locator_market_Data_1,locator_name='Market_data')

            case 3:
                return self.do_click('xpath',self.locator_Turn_up_down_2,locator_name='Turnover')

            case 4:
                return self.do_click('xpath', self.locator_1Y,  locator_name='Graph_1')


    def list_of_all_related_comp(self) -> List[WebElement]:   #Receiving list of all companies related to index TA-125
        return self.are_visible('class', self.locator_class, 'All_index_of_TA-125')


    def couple_nameComp_webElem(self) -> dict:           #Receiving dictionary{company:webelement}

         all1 = self.list_of_all_related_comp()          #List_of_Webelements
         d_text=self.get_text_from_webelements(all1)     #List_of_Text_Elements

         couple_Text_element_Webelement = {}
         for v in range(0, len(all1)):
             couple_Text_element_Webelement[d_text[v] ]= all1[v]

         return  couple_Text_element_Webelement                         #


    def output_text_file(self):
        text = self.couple_nameComp_webElem()
        timestr = time.strftime('%Y-%m-%d-%H.%M.%S')
        text_file = open(timestr, "w")
        text_file.write(
            'List of companies related to index TA-125, with all data and to sort them by Turnover (NIS thousands)')
        for text_element, _webelement in text.items():
            print(text_element)
            text_file.writelines(text_element + '\n')
        text_file.close()



    def get_nav_link_by_name(self,name) ->WebElement:
         elements = self.list_of_all_related_comp()
         return self.get_element_by_text(elements,name)




    def screen_shot(self,name):
        timestr = time.strftime('%Y-%m-%d-%H.%M.%S')

        time.sleep(2)
        self.driver.save_screenshot(f".\\Source\\{name,timestr}.png")


    def getWebelement_from_couple(self, name_company):

        return self.couple_nameComp_webElem().get(name_company, "Wrong_name_company_ENTER ANOTHER  NAME COMPANY")



# *********************************************************************************************************************

    # def if_name_List_of_Relat_comp(self, name):
    #
    #     for key, value in self.couple_nameComp_webElem().items():
    #
    #         if key == name:
    #             value.click()
    #             self.do_click('xpath', self.locator_1Y, 'Graph_1Y')
    #
    #             return key


#*********************************************************************************************************************