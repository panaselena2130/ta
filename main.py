import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
    driver.get('https://www.tase.co.il/en/')
    # element = driver.find_element(By.XPATH,'//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[3]/td[1]/a/span')
    # e=element.click()
    #************************************************************************************************************************
    spisok_index = []
    # spisok =driver.find_element(By.XPATH,'//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]td[1]/a')
    # spisok =driver.find_element(By.XPATH,'//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[4]/td[1]/a').click()
    spisok =driver.find_elements(By.XPATH,'//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr')
    #
    for e in spisok:
        print(e.text)

        if e.is_displayed():
            e.click()

    for s in spisok:
        print(s.text)
        print(type(s.text))
        spisok_index.append(s.text)


        print('_____________________________')


    for udalenie in spisok_index:
        print(udalenie)
        print("***********************************")
        for t in udalenie:
          print(t)
          print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

#
#
    leng = len(spisok_index)
    print("Length_of list_index", leng)
    # xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
    xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
    for num, i in enumerate(xpth, 0):
        print(num, i)

    position = 67

    new_character = list(range(1, leng, 1))
    # w=input('e.text')
    for i in new_character:
         i_replace = str(i)
         # print(i_replace, type(i_replace))
         xpth_new = xpth[:position] + i_replace + xpth[position + 1:]

         progon = driver.find_elements(By.XPATH,xpth_new)
         for e1 in progon:

           # print(e1.text, type(e1.text))
           new = e1.text.lstrip('Index')
           print(new,type(new))


           #
           # spl1=str(spl1)
           # print(spl1)
#     #         # spl2=spl1.split(',', maxsplit=1)
#     #         # print(spl)
#     #         # print(spl[1])
#     #
#     #         # if spl[2]== None:
#     #         #     add = spl[1]
#     #         # else:
#     #         #     add = spl[1] + spl[2]
#     #         #     print(add)
#     #         # if spl[1:] == w:
#     #         #     e.click()
#     #
#     #         # if e.text == w:
#     #         #     print(e.text)
#     #         #     e.click()
#     #
#     #     # for e in progon:
#     #     #     #print(e.text,type(e.text))
#     #     #     spl=e.text.split()
#     #     #     print(spl[1], type(spl[1]))
#     #     #
#     #     #     if spl[1] == w:
#     #     #          print("It's_Target_Index")
#     #     #          e.click()
#     #     #
#     #     #     else:
#     #     #          print('Try_again')
# #***********************************************************************************************************************************************************
#
#














    # time.sleep(5)
    # pri_ = driver.title
    # pri_split =pri_.split('|')
    # print(pri_split,type(pri_split))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
