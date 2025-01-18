class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# node is none in the last node in a linked list


def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next


head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)
print(head.next.value)
print(head.next.next.value)

iter_linked_list(head)
