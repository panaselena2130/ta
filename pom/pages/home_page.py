import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePages


class HomePage(BasePages):


    def __init__(self,driver):
        # super(HomePage, self).__init__(driver)
        super(HomePage, self).__init__(driver)


    def load_page(self):
        self.driver.get('https://www.tase.co.il/en/')






    def login(self):
        self.do_click()


    def req_index(self,driver):
        spisok_index = []
        spisok = driver.find_elements(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr')

        for s in spisok:
            spisok_index.append(s.text)

        leng = len(spisok_index)
        xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
        for num, i in enumerate(xpth, 0):
            print(num, i)

        position = 67

        new_character = list(range(1, leng + 1, 1))

        new_list=[]
        dic = {}
        h = input('input')

        for i in new_character:
                i_replace = str(i)
                xpth_new = xpth[:position] + i_replace + xpth[position + 1:]
                iter_po_spisku = driver.find_elements(By.XPATH, xpth_new)
                for e1 in iter_po_spisku:
                     d=e1.text.lstrip("Index\n")

                     dic[e1]=d
                     new_list.append(d)

        for key,value in dic.items():

            if dic[key] == h:
                self.do_click(key)
                time.sleep(2)

                a=self.do_current_url(driver)

                self.driver.get(a)

                element_metod = driver.find_element(By.XPATH,'//*[@id="mainContent"]/index-lobby/section[1]/div/div/section[2]')
                self.do_click(element_metod)









