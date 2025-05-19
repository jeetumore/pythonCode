

class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None


def linkedlist(head):
    current = head
    while current:
        print(current.data, end="-> ")
        current = current.next

    print("Null")

def reverseLinklist(head):
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

head = Node(1)
head.next= Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

#linkedlist(head)

reverselink = reverseLinklist(head)

linkedlist(reverselink)


