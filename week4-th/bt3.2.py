def selection_sort(arr,n):
    for index in range(n):
        min_index=index
        for j in range(index+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[index],arr[min_index]=arr[min_index],arr[index]
arr=[12,11,13,5,6]
n=len(arr)
selection_sort(arr,n)
print(arr)  
