xpth = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody/tr[1]/td[1]/a'

for num, i in enumerate(xpth,0):
       print(num,i)


position =67

leng = 11

new_character = list(range(1,leng,1))
print(new_character,'list')
for i in new_character:
       i_replace = str(i)
       print(i_replace, type(i_replace))
       xpth_new = xpth[:position] + i_replace + xpth[position + 1:]
       print(xpth_new)


