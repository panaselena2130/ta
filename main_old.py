from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
    driver.get('https://www.tase.co.il/en/')
    spisok_index = []
    spisok = driver.find_elements(By.XPATH, '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr')


    for s in spisok:
        print(s.text)
        print(type(s.text))
        spisok_index.append(s.text)

    leng = len(spisok_index)
    print("Length_of list_index", leng)
    print(spisok_index)
    xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'
    for num, i in enumerate(xpth, 0):
        print(num, i)

    position = 67

    new_character = list(range(1, leng+1, 1))
    w = input('new')
    for i in new_character:
            i_replace = str(i)
            # print(i_replace, type(i_replace))
            xpth_new = xpth[:position] + i_replace + xpth[position + 1:]

            iter_po_spisku = driver.find_elements(By.XPATH, xpth_new)
            for e1 in iter_po_spisku:

                new = e1.text.lstrip('Index\n')
                print(new, 'Name_of_index')


                if new == str(w):
                    e1.click()
                    print("Done_Click_Target_Index")







