
"""
CÂU 7 - Bảng băm & Mảng cộng dồn (Prefix Sum + Hash Map)

Đề bài: A = [3,4,7,2,-3,1,4,2], S=7. Đếm số mảng con có tổng bằng S
trong O(N), thay vì O(N^2) bằng 2 vòng lặp lồng nhau.
"""

# Ý tưởng: gọi prefix[i] = tổng của i phần tử đầu tiên (prefix[0] = 0).
# Một đoạn con từ chỉ số p đến q (0-index, q inclusive) có tổng bằng S
# khi và chỉ khi:  prefix[q+1] - prefix[p] = S
# Duyệt mảng, tại mỗi vị trí ta đã biết prefix hiện tại (gọi là "tong"),
# ta cần đếm xem có bao nhiêu prefix TRƯỚC ĐÓ bằng (tong - S) - dùng
# Hash Map (dict) để tra cứu trong O(1) thay vì duyệt lại O(N).

def dem_doan_con_tong_bang_s(a, s):
    dem_prefix = {0: 1}      # prefix = 0 xuất hiện 1 lần (trước khi duyệt phần tử nào)
    tong = 0
    so_doan_con = 0
    for x in a:
        tong += x
        if (tong - s) in dem_prefix:
            so_doan_con += dem_prefix[tong - s]
        dem_prefix[tong] = dem_prefix.get(tong, 0) + 1
    return so_doan_con


if __name__ == "__main__":
    a = [3, 4, 7, 2, -3, 1, 4, 2]
    s = 7

    ket_qua = dem_doan_con_tong_bang_s(a, s)

    print("Mảng A =", a, ", S =", s)
    print("Số đoạn con có tổng bằng S =", ket_qua)