
"""
CÂU 5 - Ứng dụng Hàng đợi (Deque - giá trị nhỏ nhất trong cửa sổ trượt)

Đề bài: A = [4,2,12,11,-5,8,1,5,6], k=3. Tìm giá trị NHỎ NHẤT trong mỗi
cửa sổ trượt bằng Deque. Trình bày 3 bước đầu tiên và mảng kết quả.
"""

from collections import deque

# Khác với tìm MAX (deque giảm dần), tìm MIN ta duy trì deque TĂNG DẦN:
# - Trước khi thêm phần tử mới, loại bỏ (từ cuối deque) mọi phần tử lớn
#   hơn hoặc bằng phần tử mới (vì chúng không thể là min khi phần tử mới
#   còn nằm trong cửa sổ).
# - Loại bỏ phần tử ở đầu deque nếu nó đã ra khỏi phạm vi cửa sổ hiện tại.
# - Phần tử ở đầu deque luôn là giá trị nhỏ nhất của cửa sổ hiện tại.

def min_cua_so_truot(a, k):
    dq = deque()             # lưu chỉ số, giá trị TĂNG dần từ đầu đến cuối deque
    ket_qua = []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] > x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:    # phần tử đầu deque đã ra khỏi cửa sổ
            dq.popleft()
        if i >= k - 1:
            ket_qua.append(a[dq[0]])
    return ket_qua


if __name__ == "__main__":
    a = [4, 2, 12, 11, -5, 8, 1, 5, 6]
    k = 3

    print("Mảng A =", a, ", k =", k)
    print("3 bước dịch chuyển đầu tiên của Deque:")
    print("  Bước 1 - cửa sổ [4,2,12]  : deque chứa giá trị [2,12] -> min = 2")
    print("  Bước 2 - cửa sổ [2,12,11] : deque chứa giá trị [2,11] -> min = 2")
    print("  Bước 3 - cửa sổ [12,11,-5]: deque chứa giá trị [-5]   -> min = -5")

    ket_qua = min_cua_so_truot(a, k)
    print("Mảng kết quả đầy đủ =", ket_qua)