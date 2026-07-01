# --- ĐOẠN CODE CƠ SỞ ---
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
# -----------------------

# 1. HÀM TÌM NÚT GIỮA
def tim_diem_giua(head):
    cham = head
    nhanh = head.next # Nhanh đi trước 1 nhịp để chậm dừng đúng ở nửa đầu
    while nhanh and nhanh.next:
        cham = cham.next
        nhanh = nhanh.next.next
    return cham

# 2. HÀM TRỘN 2 DANH SÁCH (Tương tự Bài 9)
def tron_danh_sach(l1, l2):
    dummy = Node(0)
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

# 3. HÀM SẮP XẾP CHÍNH (ĐỆ QUY)
def sap_xep_danh_sach(head):
    # Điều kiện dừng: Danh sách rỗng hoặc chỉ có 1 phần tử (đã tự sắp xếp)
    if not head or not head.next:
        return head
    
    # Bước 1: Tìm điểm giữa và cắt đôi
    giua = tim_diem_giua(head)
    nua_sau = giua.next
    giua.next = None # Cắt đứt liên kết chia làm 2 nửa
    
    # Bước 2: Gọi đệ quy cho từng nửa
    trai = sap_xep_danh_sach(head)
    phai = sap_xep_danh_sach(nua_sau)
    
    # Bước 3: Trộn 2 nửa lại với nhau
    return tron_danh_sach(trai, phai)

# --- CHẠY THỬ THỰC TẾ ---
if __name__ == "__main__":
    # Tạo danh sách theo ví dụ: 3 -> 1 -> 2
    node1 = Node(3, Node(1, Node(2)))
    
    print("Trước khi sắp xếp:")
    in_danh_sach(node1)
    
    # Gọi hàm sắp xếp
    head_da_sap_xep = sap_xep_danh_sach(node1)
    
    print("Sau khi sắp xếp:")
    in_danh_sach(head_da_sap_xep)