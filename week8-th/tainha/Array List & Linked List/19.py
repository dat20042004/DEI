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


def chen_sau(node_truoc, val):
    if not node_truoc:
        return
    # Nút mới trỏ tới nút đứng sau của node_truoc
    node_moi = Node(val, node_truoc.next)
    # node_truoc trỏ tới nút mới
    node_truoc.next = node_moi

if __name__ == "__main__":
    node1 = Node(1, Node(3)) # Danh sách: 1 -> 3
    
    chen_sau(node1, 2) # Chèn số 2 ngay sau node1
    in_danh_sach(node1) # Kết quả: 1 -> 2 -> 3 -> None