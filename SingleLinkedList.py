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

            while (itr):
                print()
                print(" przejście ", i)
                i += 1
                if itr == remove and x == 1:
                    print("if")
                    print("if itr", itr)
                    print("if itr value", itr.value)
                    temp = itr
                    itr = itr.next
                    x = 2
                else:
                    print("else")
                    print("else itr", itr)
                    print("else temp", temp)
                    print("else temp value", temp.value)
                    print("else head", self.head)
                    print("else head value", self.head.value)
                    itr = itr.next
                if x == 2:
                    print("jestem")
                    itr = temp  # tutaj powinna być podmiana
                    x = 3


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