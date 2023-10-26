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

    def remove(self, remove):
        if not self.head:
            raise ValueError()
        else:
            itr = self.head
            temp = Node(0)
            i = 1
            x = 1

            while (itr.next):
                if itr.next == remove:
                    print("if")
                    print("if itr", itr.next)
                    print("if itr value", itr.value)
                    itr.next = itr.next.next
                    x = 2
                itr = itr.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


'''lista_testowa = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
lista_testowa.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
lista_testowa.remove(node3)
i = 2
'''
