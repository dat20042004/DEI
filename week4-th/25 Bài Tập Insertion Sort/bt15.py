class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_insertion_sort(head):
    if not head or not head.next:
        return head
        
    sorted_head = None  # Danh sách mới đã sắp xếp
    curr = head
    
    while curr:
        next_node = curr.next  # Lưu lại nút tiếp theo
        
        # Tìm vị trí chèn nút `curr` vào `sorted_head`
        if not sorted_head or sorted_head.data >= curr.data:
            curr.next = sorted_head
            sorted_head = curr
        else:
            search = sorted_head
            while search.next and search.next.data < curr.data:
                search = search.next
            curr.next = search.next
            search.next = curr
            
        curr = next_node
    return sorted_head

# Chạy thử nghiệm
h = Node(3); h.next = Node(1); h.next.next = Node(2)
sorted_h = linked_list_insertion_sort(h)
res = []
while sorted_h:
    res.append(sorted_h.data)
    sorted_h = sorted_h.next
print(res)  # Kết quả: [1, 2, 3]