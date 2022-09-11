


from pom.pages.home_page import HomePage

def test_login(driver):
    print('___________')
    homepage = HomePage(driver)
    homepage.load_page()
    homepage.req_index(driver)



