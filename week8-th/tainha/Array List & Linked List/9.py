arr = [1, 2, 3, 4]
trai, phai = 0, len(arr) - 1
while trai < phai:
    arr[trai], arr[phai] = arr[phai], arr[trai] # Đổi chỗ
    trai += 1
    phai -= 1
print("Đảo ngược:", arr)