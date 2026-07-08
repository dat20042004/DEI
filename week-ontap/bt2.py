
"""
CÂU 2 - Thuật toán Sắp xếp (Insertion Sort & số nghịch thế)

Đề bài: A = [5,2,4,6,1,3]. Tính tổng số lần dịch chuyển (shift) khi
Insertion Sort mảng tăng dần. Mối liên hệ với số nghịch thế (inversions)?
"""

# GIẢI THÍCH:
# Insertion sort: mỗi khi chèn phần tử key vào đúng vị trí trong phần đã
# sắp xếp, ta phải dịch (shift) các phần tử lớn hơn key sang phải 1 vị trí.
# Mỗi lần shift tương ứng CHÍNH XÁC với 1 cặp nghịch thế (một cặp i<j mà
# a[i] > a[j]) bị "giải quyết". Vì vậy:
#       Tổng số shift  ==  Tổng số nghịch thế của mảng ban đầu.

def insertion_sort_dem_shift(a):
    a = a[:]
    so_shift = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            so_shift += 1
        a[j + 1] = key
    return a, so_shift


def dem_nghich_the_On2(a):
    n = len(a)
    dem = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                dem += 1
    return dem


if __name__ == "__main__":
    a = [5, 2, 4, 6, 1, 3]
    da_sap_xep, so_shift = insertion_sort_dem_shift(a)
    so_nghich_the = dem_nghich_the_On2(a)

    print("Mảng ban đầu     =", a)
    print("Mảng sau sắp xếp =", da_sap_xep)
    print("Tổng số shift    =", so_shift)
    print("Số nghịch thế    =", so_nghich_the)
    print("=> Hai giá trị BẰNG NHAU:", so_shift == so_nghich_the)