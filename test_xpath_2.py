#//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[2]/td[1]/a

import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List


driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
driver.get('https://www.tase.co.il/en/')


elements: WebDriver = driver.find_element(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[9]/td[1]/a').click()
time.sleep(2)
#elements: WebDriver = driver.find_element(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[3]').click()
print(driver.title, "Title")
