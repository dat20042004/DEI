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


def xoa_nut(head, val):
    # Nếu nút cần xóa là nút đầu tiên
    if head and head.val == val:
        return head.next
    
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next # Nhảy cóc qua nút cần xóa
            break
        curr = curr.next
    return head

if __name__ == "__main__":
    node1 = Node(1, Node(2, Node(3, Node(2)))) # 1 -> 2 -> 3 -> 2
    node1 = xoa_nut(node1, 2)
    in_danh_sach(node1) # Kết quả: 1 -> 3 -> 2 -> None (chỉ xóa số 2 đầu tiên)