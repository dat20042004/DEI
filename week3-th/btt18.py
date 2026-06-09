class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sort_linked_list(dau):
    doi = True
    while doi:
        doi = False
        hien_tai = dau
        while hien_tai.next:
            if hien_tai.val > hien_tai.next.val:
                hien_tai.val, hien_tai.next.val = hien_tai.next.val, hien_tai.val
                doi = True
            hien_tai = hien_tai.next
    return dau

# Tạo linked list: 1 -> 3 -> 2
n1 = Node(1); n2 = Node(3); n3 = Node(2)
n1.next = n2; n2.next = n3

dau = sort_linked_list(n1)
hien_tai = dau
while hien_tai:
    print(hien_tai.val, end=" -> ")
    hien_tai = hien_tai.next
print("null")