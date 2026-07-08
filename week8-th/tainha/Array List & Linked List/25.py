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


def xoa_nut_cuoi_thu_k(head, k):
    dummy = Node(0, head)
    cham = nhanh = dummy
    
    for _ in range(k + 1):
        nhanh = nhanh.next
        
    while nhanh:
        cham = cham.next
        nhanh = nhanh.next
        
    cham.next = cham.next.next
    return dummy.next

if __name__ == "__main__":
    node1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head_moi = xoa_nut_cuoi_thu_k(node1, 2) # Xóa nút thứ 2 từ cuối (số 4)
    in_danh_sach(head_moi)