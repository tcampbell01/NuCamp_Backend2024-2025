class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Prepended new Head Node with value:", self.head.value)
            print("Node following Head is: ", node.next)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)


llist = LinkedList()
llist.prepend("first node")
llist.prepend("Inserted New First Node")
