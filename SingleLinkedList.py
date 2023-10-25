class SingleLinkedList:
    def __init__(self):
        self.head = None
        # self.list = []

    def clear(self):
        self.head = None

    def append(self, append):
        if not self.head:
            self.head = Node(append)
        else:
            itr = self.head
            while (itr.next):
                itr = itr.next
            itr.next = Node(append)

    def remove(self):
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

test = SingleLinkedList()
test.head = node1
node1.next = node2
node2.next = node3

