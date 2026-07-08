
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

def tron_danh_sach(l1, l2):
    dummy = Node(0) # Nút giả để làm mỏ neo
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

if __name__ == "__main__":
    l1 = Node(1, Node(3, Node(5)))
    l2 = Node(2, Node(4))
    ket_qua = tron_danh_sach(l1, l2)
    in_danh_sach(ket_qua) # Kết quả: 1 -> 2 -> 3 -> 4 -> 5 -> None