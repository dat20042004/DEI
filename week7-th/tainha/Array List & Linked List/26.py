
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


class DoubleNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def them_dau(head, val):
    node_moi = DoubleNode(val)
    if head:
        head.prev = node_moi
        node_moi.next = head
    return node_moi

if __name__ == "__main__":
    head = None
    head = them_dau(head, 20)
    head = them_dau(head, 10)
    print(f"{head.val} <-> {head.next.val}") # Kết quả: 10 <-> 20