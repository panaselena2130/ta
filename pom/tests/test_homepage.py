
from pom.pages.home_page import HomePage

def test_login(driver):
    print('___________')
    homepage = HomePage(driver)
    homepage.load_page()


    

    print(homepage.text_of_list_Ind_Homepage())

    homepage.major_data()
    print(homepage.text_of_list_relat_company())
    (homepage.output_text_file())

   
