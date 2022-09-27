
from pom.pages.home_page import HomePage

def test_login(driver):
    print('___________')
    homepage = HomePage(driver)
    homepage.load_page()
    # actual_links = homepage.text_of_list_Ind_Homepage()
    # expected_links = homepage.LINK_TEXT
    # assert expected_links==actual_links

    print(homepage.text_of_list_Ind_Homepage())
    homepage.major_data()
    print(homepage.text_of_list_relat_company())
    homepage.output_text_file()

    # homepage.req_index(driver)

    # homepage.input()

