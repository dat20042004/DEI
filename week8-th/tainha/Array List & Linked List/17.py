class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# BƯỚC 1: Đưa hàm ra ngoài Class (xóa thụt lề đầu dòng)
def duyet_va_dem(head):
    dem = 0
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        dem += 1
        curr = curr.next
    print("None")
    return dem

# BƯỚC 2: Chạy thử thực tế
if __name__ == "__main__":
    # Tạo các nút
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    # Nối các nút lại với nhau (10 -> 20 -> 30)
    node1.next = node2
    node2.next = node3

    # Gọi hàm và truyền nút đầu tiên (node1) vào làm head
    tong_so_nut = duyet_va_dem(node1)
    print("Tổng số nút đếm được là:", tong_so_nut)