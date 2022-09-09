#
#
# import time
# from selenium import webdriver
# import pytest
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
# from typing import List
#
# #if __name__ == '__main__':
#
# #def setup_driver()->webdriver:
# driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
# driver.get('https://www.tase.co.il/en/')
#
# #requared_name = input('type requared_name')
#
# elements:List[WebElement] = driver.find_elements(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr')
# # elements1 = driver.find_element(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[3]/td[1]/a')
# # elements2 = driver.find_element(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[9]/td[1]/a')
# list:List[WebElement]= elements
#
# #e2=elements2.click()
#
# # print(type(elements),'type=')
# # print(type(list),'type=list',list)
# for i in list:
#     #print(i.text, 'iiiiiiiiii', type(i.text), 'type - i.text')
#     print(i.text,'i.text',type(i.text))
#     razdel=i.text.split()
#     print(razdel, 'after_split')
#
#     #if razdel[1] ==requared_name:
#
#
#
#
#
# # index_TA = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[4]/td[1]/a/text()'
#
#
# # li = list(index_TA)
# # print(type(li))
#
#
#
#
#
#
#
#
#
#
#
#
