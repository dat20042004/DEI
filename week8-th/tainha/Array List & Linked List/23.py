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




def tim_chu_trinh(head):
    cham = nhanh = head
    while nhanh and nhanh.next:
        cham = cham.next
        nhanh = nhanh.next.next
        if cham == nhanh: # Gặp nhau -> Có chu trình
            
            # Khúc này là Bài 12: Tìm điểm bắt đầu
            cham = head
            while cham != nhanh:
                cham = cham.next
                nhanh = nhanh.next
            return True, cham.val # Trả về Có chu trình và Giá trị nút bắt đầu
            
    return False, None

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node2 # Tạo chu trình vòng ngược lại nút 2
    
    co_chu_trinh, diem_bat_dau = tim_chu_trinh(node1)
    print(f"Có chu trình không? {co_chu_trinh}. Điểm bắt đầu: {diem_bat_dau}")