


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def traversalLinkList(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next

    print("NULL")

def reverseLinkList(head):
    prev = None
    current = head

    while current:
        net_node = current.next
        current.next = prev
        prev = current
        current = net_node

    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:")
traversalLinkList(head)

rev = reverseLinkList(head)

print(traversalLinkList(rev))