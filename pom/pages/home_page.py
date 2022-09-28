import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePages

from typing import List
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePages):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver
        #self.locator_home_page: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody'
        self.locator_home_page: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr'
        self.locator_TA_35: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
        self.locator_TA_125_Fossill: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[2]/td[1]/a'
        self.locator_TA_125: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[3]/td[1]/a'
        self.locator_TA_Finance: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[4]/td[1]/a'
        self.locator_Cleantech: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[5]/td[1]/a'
        self.locator_TA_Retail: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[6]/td[1]/a'
        self.locator_TA_Sector_Balance: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[7]/td[1]/a'
        self.locator_All_Bond: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[8]/td[1]/a'
        self.locator_Bond_CPI_A: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[9]/td[1]/a'
        self.locator_Tel_Bond_60: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[10]/td[1]/a'
        self.locator_More_about: str = '//*[@id="mainContent"]/index-lobby/section[1]/div/div/section[2]'
        self.locator_Index_component: str = '//*[@id="more_madad_nav"]/ul/li[1]/ul/li[4]/a'
        self.locator_market_Data:str = '#mainContent > index-lobby > index-composition > index-weight > gridview-lib > div > div.container > div > filter-data > div > div.table_sorting_box > div > div.table_sorting_separator.no_border > div > label:nth-child(4)'
        self.locator_Turn_up_down:str = '#mainContent > index-lobby > index-composition > index-market-data > gridview-lib > div > div.container > div > div > div.table_page_table_container > table > thead > tr.sort-btns > td:nth-child(6) > ul > li:nth-child(2) > button'
        self.locator_Company:str = '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody'



    def load_page(self):
        self.driver.get('https://www.tase.co.il/en/')

    def list_of_Ind_Homepage(self) -> List[WebElement]:
        return self.are_visible('xpath', self.locator_home_page, 'All_index_of_HomePage')

    def text_of_list_Ind_Homepage(self) -> str:

        all = self.list_of_Ind_Homepage()

        d_text=[i.text for i in all]

        return ",".join(d_text)



    def major_data(self):
        self.do_click('xpath',self.locator_TA_125,'TA-125')
        self.do_click('xpath',self.locator_More_about,'More_About')
        self.do_click('xpath',self.locator_Index_component,'Index_component')
        self.do_click('css',self.locator_market_Data,'Market_data')
        self.do_click('css',self.locator_Turn_up_down,'Turnover')

    def list_of_relat_company(self)-> List[WebElement]:
        return self.are_visible('xpath', self.locator_Company, 'Related')



    def text_of_list_relat_company(self) -> str:

        all_relat = self.list_of_relat_company()

        d_relat_text=[i.text for i in all_relat]

        return ",".join(d_relat_text)

    def output_text_file(self):
        text=self.text_of_list_relat_company()
        e=text.split()

        for r in e:
             if r ==  'לפעולות':
                e.remove(r)
        for r in e:
             if r ==  'לינקים':
                e.remove(r)
        for r in e:
             if r == 'שונות':
                 e.remove(r)


        text_file=open("file1.txt","w")
        for index in e:
            text_file.write(index+ ' ' + '\n')

        text_file.close()



