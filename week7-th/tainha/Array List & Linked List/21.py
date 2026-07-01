
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

def dao_nguoc(head):
    truoc = None
    hien_tai = head
    while hien_tai:
        tam = hien_tai.next
        hien_tai.next = truoc # Lật ngược mũi tên
        truoc = hien_tai
        hien_tai = tam
    return truoc

if __name__ == "__main__":
    node1 = Node(1, Node(2, Node(3)))
    head_moi = dao_nguoc(node1)
    in_danh_sach(head_moi) # Kết quả: 3 -> 2 -> 1 -> None