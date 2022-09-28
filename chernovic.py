all =  [1, 'seva','misha']

all = [str(i) for i in all]

print(all,type(all))

all_1=(",".join(all))
print(all_1,type(all_1))

for i in all:
    if i == 'seva':
        print("ok")
