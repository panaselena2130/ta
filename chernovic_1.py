import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pom.pages.base_page import BasePages
from pom.pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ec
import re
if __name__ == '__main__':


    driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.tase.co.il/en/market_data/security/273011/major_data')
    driver.get('https://www.tase.co.il/en/market_data/index/137/major_data')
    try:
        title=driver.title
        assert 'TA-125' in title
        print("Assertion_test_pass")
        print(title)
    except Exception as e:
        print("Assertion test failed", format(e))



    food_item = input(("Enter Food Item Name"))

    food_item_dict = {'Burger':100,'Pizza':200,'Juice':50,'Tofu':150}
    def getPrice(food_item):
            return food_item_dict.get(food_item,"No")
    print(getPrice(food_item))







    # spisok = WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
    #                                                                     '#mainContent > index-lobby > index-composition > index-weight > gridview-lib > div > div.container > div > filter-data > div > div.table_sorting_box > div > div.table_sorting_separator.no_border > div > label:nth-child(4)')))
    # spisok.click()
    #
    # spisok_comp = driver.find_elements(By.XPATH,
    #                                    '//*[@id="mainContent"]/index-lobby/index-composition/index-market-data/gridview-lib/div/div[2]/div/div/div[2]/table/tbody')
    # spisok_t = WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
    #                                                                      '#mainContent > index-lobby > index-composition > index-market-data > gridview-lib > div > div.container > div > div > div.table_page_table_container > table > thead > tr.sort-btns > td:nth-child(6) > ul > li:nth-child(2) > button')))
    #
    #
    # spisok_t.click()
    #
    # for i in spisok_comp:
    #     a = i.text
    #
    #
    #     data = a.split('\n')
    #
    #
    #     for g in data:
    #          if g == 'לינקים לפעולות שונות':
    #              data.remove(g)
    #
    #     for g in data:
    #          if g == 'DL':
    #              data.remove(g)
    #
    #
    #     for g in data:
    #         if g == 'MM':
    #             data.remove(g)
    #
    #
    #     f=open('lena.txt','w')
    #     for index in data:
    #         f.write(index+' '+'\n')
    #     f.close()
    #
    #
    #
    # print(data,'DATA')
    #
