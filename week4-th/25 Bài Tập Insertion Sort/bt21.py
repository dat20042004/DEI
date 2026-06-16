# Sử dụng cấu trúc giải thuật Merge Sort để đếm số cặp nghịch thế (bằng tổng số shift) với chi phí O(n log n)
def merge_and_count(a, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid + 1
    k = left
    
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            inv_count += (mid - i + 1)  # Toàn bộ phần tử còn lại ở nhánh trái đều tạo cặp nghịch thế với a[j]
            j += 1
        k += 1
        
    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = a[j]
        j += 1
        k += 1
        
    for idx in range(left, right + 1):
        a[idx] = temp[idx]
        
    return inv_count

def merge_sort_count(a, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_count(a, temp, left, mid)
        inv_count += merge_sort_count(a, temp, mid + 1, right)
        inv_count += merge_and_count(a, temp, left, mid, right)
    return inv_count

large_arr = [2, 4, 1, 3] * 25000  # Tạo mảng lớn kích thước 10^5
temp_arr = [0] * len(large_arr)
print("Tổng số shift tính được (O(n log n)): ", merge_sort_count(large_arr, temp_arr, 0, len(large_arr) - 1))