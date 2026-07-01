def tim_kiem(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Vị trí của 7 là:", tim_kiem([5, 3, 7], 7))