import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePages


class HomePage(BasePages):

    def __init__(self, driver):
        # super(HomePage, self).__init__(driver)
        super(HomePage, self).__init__(driver)

    def load_page(self):
        self.driver.get('https://www.tase.co.il/en/')

    def login(self):
        self.do_click()

    def req_index(self, driver):
        spisok_index = []
        spisok = driver.find_elements(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr')
        locator_market = (By.CSS_SELECTOR,
                          '#mainContent > index-lobby > index-composition > index-weight > gridview-lib > div > div.container > div > filter-data > div > div.table_sorting_box > div > div.table_sorting_separator.no_border > div > label:nth-child(4)')

        locator_Turn = ((By.CSS_SELECTOR,
                         '#mainContent > index-lobby > index-composition > index-market-data > gridview-lib > div > div.container > div > div > div.table_page_table_container > table > thead > tr.sort-btns > td:nth-child(6) > ul > li:nth-child(2) > button'))

        locator_list_company = (By.XPATH,
                                '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody')

        for s in spisok:
            spisok_index.append(s.text)

        leng = len(spisok_index)
        xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
        for num, i in enumerate(xpth, 0):
            print(num, i)

        position = 67

        new_character = list(range(1, leng + 1, 1))

        new_list = []
        dic = {}
        h = input('input')

        for i in new_character:
            i_replace = str(i)
            xpth_new = xpth[:position] + i_replace + xpth[position + 1:]
            iter_po_spisku = driver.find_elements(By.XPATH, xpth_new)
            for e1 in iter_po_spisku:
                d = e1.text.lstrip("Index\n")

                dic[e1] = d
                new_list.append(d)

        for key, value in dic.items():

            if dic[key] == h:
                self.do_click(key)
                time.sleep(2)

                a = self.do_current_url(driver)

                self.driver.get(a)

                self.do_click(locator=(By.XPATH, '//*[@id="mainContent"]/index-lobby/section[1]/div/div/section[2]'))  # More about
                self.do_click(locator=(By.XPATH, '//*[@id="more_madad_nav"]/ul/li[1]/ul/li[4]/a'))  # Index component
                self.do_click(locator_market)  # Market Data
                spis_comp = driver.find_elements(By.XPATH,
                                                 '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody')  # List of company
                self.do_click(locator_Turn)  # Turnover_click

                for i in spis_comp:
                    u = i.text

                    data = u.split('\n')

                    for g in data:
                        if g == 'לינקים לפעולות שונות':
                            data.remove(g)

                    for g in data:
                        if g == 'DL':
                            data.remove(g)

                    for g in data:
                        if g == 'MM':
                            data.remove(g)

                    f = open('lena8.txt', 'w')
                    for index in data:
                        f.write(index + ' ' + '\n')
                    f.close()

                print(data, 'DATA')










