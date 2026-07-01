
# --- ĐOẠN CODE CƠ SỞ (LUÔN ĐỂ Ở ĐẦU FILE) ---
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def in_danh_sach(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
# ---------------------------------------------

def cong_hai_so(l1, l2):
    dummy = Node(0)
    curr = dummy
    nho = 0
    while l1 or l2 or nho:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        tong = v1 + v2 + nho
        
        nho = tong // 10       # Lấy số chục để nhớ
        curr.next = Node(tong % 10) # Lưu số đơn vị
        curr = curr.next
        
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

if __name__ == "__main__":
    # Biểu diễn số 342 (viết ngược 2 -> 4 -> 3)
    so1 = Node(2, Node(4, Node(3)))
    # Biểu diễn số 465 (viết ngược 5 -> 6 -> 4)
    so2 = Node(5, Node(6, Node(4)))
    
    ket_qua = cong_hai_so(so1, so2) # 342 + 465 = 807 (Ngược: 7 -> 0 -> 8)
    in_danh_sach(ket_qua)