import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.pages.base_page import BasePages
from pom.pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
    driver.get('https://www.tase.co.il/en/')
    print(driver, 'driver')
    spisok_index = []
    spisok = driver.find_elements(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr')


# +++++++++++++++++++++Block_Poisk_Index+++++++++++++++++++++++++++++++++++++++++++++++++
def Poisk_Req_name():
    for s in spisok:
        print(s.text)
        print(type(s.text))
        spisok_index.append(s.text)

    leng = len(spisok_index)
    print("Length_of list_index", leng)
    print(spisok_index)
    xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
    # for num, i in enumerate(xpth, 0):
    # print(num, i)

    position = 67

    new_character = list(range(1, leng + 1, 1))

    w = input('new')
    dic = {}

    for i in new_character:
        i_replace = str(i)
        # print(i_replace, type(i_replace))
        xpth_new = xpth[:position] + i_replace + xpth[position + 1:]

        iter_po_spisku = driver.find_elements(By.XPATH, xpth_new)
        for e1 in iter_po_spisku:
            new = e1.text.lstrip('Index\n')
            dic[e1] = new

    for key, value in dic.items():
        if dic[key] == w:
            key.click()
            time.sleep(2)

            print(driver.current_url)
            driver.get(driver.current_url)
            d1=driver.find_element(By.XPATH,'//*[@id="mainContent"]/index-lobby/section[1]/div/div/section[2]')
            d1.click()
            d2=driver.find_element(By.XPATH,'//*[@id="more_madad_nav"]/ul/li[1]/ul/li[4]/a')
            d2.click()



            spisok1 = WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#mainContent > index-lobby > index-composition > index-weight > gridview-lib > div > div.container > div > filter-data > div > div.table_sorting_box > div > div.table_sorting_separator.no_border > div > label:nth-child(4)')))

            spisok1.click()

            spisok_comp = driver.find_elements(By.XPATH,
                                       '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody')
            spisok_t = WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                           '#mainContent > index-lobby > index-composition > index-market-data > gridview-lib > div > div.container > div > div > div.table_page_table_container > table > thead > tr.sort-btns > td:nth-child(6) > ul > li:nth-child(2) > button')))
            spisok_t.click()

            print(type(spisok_comp))

            for i in spisok_comp:
                print(i.text, type(spisok_comp))

#
Poisk_Req_name()
