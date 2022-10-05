from selenium import webdriver
from selenium.webdriver.common.by import By





from pom.tests.test_homepage import test_login


def setup_driver() -> webdriver:
    dr:webdriver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
    dr.maximize_window()
    return dr


def close_driver(dr : webdriver):
    dr.close()
    dr.quit()

if __name__ == '__main__':
    driver = setup_driver()
    test_login(driver)







