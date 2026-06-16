import sys
arr=[12,11,13,5,6]
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr)
for i in range(len(arr)):
    print("%d" %arr[i])
