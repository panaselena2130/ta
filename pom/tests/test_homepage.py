import time

from pom.pages.home_page import HomePage

def test_login(driver):
    print('___________')
    homepage = HomePage(driver)
    homepage.load_page()
    homepage.major_data()
    print(homepage.list_of_Ind_Homepage(),'1')
    print(homepage.text_of_list_Ind_Homepage(),'2')


    y=homepage.get_nav_link_by_name('LEUMI')
    time.sleep(5)
    y.click()




   
