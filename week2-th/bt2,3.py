# Binary_Search
def binary_search(arr, left, right,key ):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, left, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, right, key)
    else:
        # Khong tim thay

        return -1
arr = [1,3,9,10,40,52,55,180,250,350]
key=250
result = binary_search(arr, 0, len(arr)-1, key)
if result != -1:
    print("Vi tri tim thay thu i la: ", result)
else:    
    print("Khong tim thay phan tu trong mang")