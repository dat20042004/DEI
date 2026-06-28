class Node:
    def __init__(self, data):
        self.data = data  # data
        self.next = None  # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(11)
    third = Node(12)

    llist.head.next = second   # Link first with second
    second.next = third        # Link second with the third
    llist.printList()
