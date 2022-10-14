import time
import datetime

from pom.pages.home_page import HomePage

def test_login(driver):



    print('___________')
    homepage = HomePage(driver)
    homepage.load_page()
    homepage.major_data()
    time.sleep(3)

    #print(homepage.list_of_Relat_comp(),'1')
    #print(homepage.text_of_list_Relat_comp(),'2')

    homepage.output_text_file()



    homepage.if_name_List_of_Relat_comp()
























