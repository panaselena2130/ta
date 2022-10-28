import time
import datetime

from pom.pages.home_page import HomePage
from pom.pages.base_page import BasePages


def test_login(driver):
    print('___________')
    homepage = HomePage(driver)
    homepage.load_page()
    homepage.verific_page()  # Verification webpage if actual_title==expected_title


    homepage.major_data(0)  # Click button 'More_about'
    time.sleep(3)
    homepage.major_data(1)  # Click button 'Index_component'
    time.sleep(15)
    homepage.major_data(2)  # Click button 'Market_data'
    time.sleep(3)
    homepage.major_data(3)  # Click button 'Turnover' for sort company  (NIS thousands) '
    time.sleep(3)

    homepage.couple_nameComp_webElem()

    homepage.output_text_file()  # The output is the text file.

    Req_comp1 = input('Enter Company Item Name').upper()

    y = homepage.getWebelement_from_couple(Req_comp1)  # Receiving webelement suitable for Req_company

    print('{}'.format(y))

    y.click()

    homepage.major_data(4)  # Click button 'Graph_1'

    homepage.verific_page()  # Verification webpage if actual_title==expeted_title

    homepage.screen_shot(Req_comp1)

    # **********************************************************************************************************************

    # t=homepage.if_name_List_of_Relat_comp(Req_comp1)
    # #
    # homepage.verific_page()
    # #
    # if Req_comp1==t:
    #
    #       homepage.screen_shot(Req_comp1)
    # else:
    #       print("ENTER ANOTHER COMPANY NAME")
    #    #
    #    #
    # print(homepage.getWebelement('TEVA'),"TEVA")
    # #

    # *********************************************************************************************************************
