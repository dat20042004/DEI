
"""
CÂU 6 - Danh sách liên kết (nguyên lý toán học của Floyd - giai đoạn 2)

Đề bài: Giải thích nguyên lý toán học khi đưa 1 con trỏ về Head, sau đó
cả 2 con trỏ cùng đi 1 bước mỗi nhịp để tìm nút bắt đầu chu trình.
"""

# GIẢI THÍCH:
# Gọi:
#   μ (mu)     = số bước đi từ Head đến điểm BẮT ĐẦU chu trình (entry point)
#   λ (lambda) = độ dài chu trình (số nút trong vòng lặp)
#   k          = khoảng cách (theo chiều đi) từ entry point đến điểm 2 con
#                trỏ gặp nhau lần đầu, tính bên trong chu trình
#
# Khi rùa (chậm) và thỏ (nhanh) gặp nhau lần đầu:
#   - Rùa đã đi:   μ + k         bước
#   - Thỏ đã đi:   2(μ + k)      bước (do thỏ đi nhanh gấp đôi rùa)
#
# Vì thỏ đã đi vòng thêm được đúng "n" vòng chu trình so với rùa (cả 2 đều
# ở trong chu trình khi gặp nhau), nên hiệu quãng đường phải là bội số của λ:
#       2(μ+k) - (μ+k) = μ + k = n·λ      (n là số nguyên dương)
#   =>  μ = n·λ - k
#
# Vì μ = n·λ - k, ta có μ ≡ -k (mod λ), tức là μ ≡ (λ - k) (mod λ).
# Nghĩa là: đi từ Head thêm μ bước sẽ đến entry point, và đi từ điểm gặp
# nhau thêm (λ - k) bước (đúng bằng phần còn lại của chu trình) CŨNG đến
# entry point - vì (λ-k) mod λ và μ mod λ là như nhau.
#
# => Do đó nếu đặt lại 1 con trỏ ở Head, giữ nguyên 1 con trỏ ở điểm gặp
#    nhau, rồi CẢ HAI cùng đi 1 bước mỗi nhịp, chúng chắc chắn sẽ gặp lại
#    nhau chính xác tại entry point của chu trình sau đúng μ bước.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def tao_linked_list_co_chu_trinh(gia_tri, vi_tri_bat_dau_chu_trinh):
    """Tạo linked list, nối đuôi về nút ở vi_tri_bat_dau_chu_trinh (0-index) để tạo chu trình."""
    cac_nut = [Node(v) for v in gia_tri]
    for i in range(len(cac_nut) - 1):
        cac_nut[i].next = cac_nut[i + 1]
    cac_nut[-1].next = cac_nut[vi_tri_bat_dau_chu_trinh]
    return cac_nut[0], cac_nut[vi_tri_bat_dau_chu_trinh]


def tim_dau_chu_trinh_floyd(head):
    cham = head
    nhanh = head
    while nhanh and nhanh.next:
        cham = cham.next
        nhanh = nhanh.next.next
        if cham == nhanh:                # giai đoạn 1: phát hiện chu trình
            p = head
            while p != cham:             # giai đoạn 2: tìm điểm bắt đầu chu trình
                p = p.next
                cham = cham.next
            return p
    return None


if __name__ == "__main__":
    head, nut_bat_dau_that_su = tao_linked_list_co_chu_trinh([1, 2, 3, 4, 5], 2)
    nut_tim_duoc = tim_dau_chu_trinh_floyd(head)

    print("Nút bắt đầu chu trình thật sự có giá trị  =", nut_bat_dau_that_su.val)
    print("Nút thuật toán Floyd tìm được có giá trị  =", nut_tim_duoc.val)
    print("Khớp nhau:", nut_tim_duoc is nut_bat_dau_that_su)