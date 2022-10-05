all =  [1, 'seva','misha']

all = [str(i) for i in all]

print(all,type(all))

all_1=(",".join(all))
print(all_1,type(all_1))

for i in all:
    if i == 'seva':
        print("ok")




lis=['Index\nTA-35\nValue\n1,837.23\nDown\n-2.05%', 'Index\nTA-125 Fossil Free\nValue\n1,798.79\nDown\n-1.79%', 'Index\nTA-125\nValue\n1,883.93\nDown\n-1.79%', 'Index\nTA Finance\nValue\n3,015.93\nDown\n-2.64%', 'Index\nCleantech\nValue\n787.61\nDown\n-0.62%', 'Index\nTA-Retail\nValue\n1,340.43\nDown\n-0.28%', 'Index\nTA Sector-Balance\nValue\n2,129.63\nDown\n-1.38%', 'Index\nAll-Bond\nValue\n365.97\nDown\n-0.25%', 'Index\nBond-CPI A\nValue\n343.06\nDown\n-0.52%', 'Index\nTel-Bond 60\nValue\n352.92\nDown\n-0.29%']
lis1=['Index\nTA-35\nValue\n1,837.23\nDown\n-2.05%', 'Index\nTA-126 Fossil Free\nValue\n1,798.79\nDown\n-1.79%', 'Index\nTA-125\nValue\n1,883.93\nDown\n-1.79%', 'Index\nTA Finance\nValue\n3,015.93\nDown\n-2.64%', 'Index\nCleantech\nValue\n787.61\nDown\n-0.62%', 'Index\nTA-Retail\nValue\n1,340.43\nDown\n-0.28%', 'Index\nTA Sector-Balance\nValue\n2,129.63\nDown\n-1.38%', 'Index\nAll-Bond\nValue\n365.97\nDown\n-0.25%', 'Index\nBond-CPI A\nValue\n343.06\nDown\n-0.52%', 'Index\nTel-Bond 60\nValue\n352.92\nDown\n-0.29%']
a='TA-35'

o=len(lis)
print(o)
for t in lis:

    print(t.split('\n'),'*****',type(t))
    if a in t.split('\n'):
        print("Here")

assert lis==lis1


string = 'lena seva misha oles'

if 'lena' in string:
    print('here')