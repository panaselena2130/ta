string = 'lena seva misha oles'
string1=[]


if 'lena' in string:
    print('found')



def search(arr,N,x):
    for i in range(0,N):
        if (arr[i]==x):
            return arr[i]



arr=['lena','seva','misha']
x='lena'
N=len(arr)
result=search(arr,N,x)
print(result)
