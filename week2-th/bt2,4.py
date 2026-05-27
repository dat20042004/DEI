# Cấu trúc giải thuật lấy đúng theo trang 37 của file
def binary_search(arr, left, right, key):
    if (right >= left):
        mid = (left + right) // 2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            return binary_search(arr, left, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, right, key)
    else:
        # khong tim thay
        return -1

# Khai báo mảng và chạy thử nghiệm đúng theo yêu cầu trang 38
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

# a) Key x = 95
key = 95
result = binary_search(arr, 0, len(arr) - 1, key)
print("a) x=95")
if (result != -1):
    print("vi tri tim thay thu i la:", str(result))
else:
    print("khong tim thay phan tu trong mang")

# b) Key x = 5
key = 5
result = binary_search(arr, 0, len(arr) - 1, key)
print("b) x=5")
if (result != -1):
    print("vi tri tim thay thu i la:", str(result))
else:
    print("khong tim thay phan tu trong mang")