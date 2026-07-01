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


def tim_nut_giua(head):
    cham = head
    nhanh = head
    while nhanh and nhanh.next:
        cham = cham.next           # Đi 1 bước
        nhanh = nhanh.next.next    # Đi 2 bước
    return cham.val if cham else None

if __name__ == "__main__":
    node1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print("Nút ở giữa là:", tim_nut_giua(node1)) # Kết quả: 3