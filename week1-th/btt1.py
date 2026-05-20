def tuyentinh(array,n,x):
    for i in range (0,n):
        if (array[i]==x):
            return i
    return -1 
array=[20,30,15,5,10,40]
x=40
n=len(array)
result=tuyentinh(array,n,x)
print('Phan tu tim thay duoc tại vi tri la:', result)
