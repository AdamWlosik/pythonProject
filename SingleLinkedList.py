class SingleLinkedListGenerator:
    def __init__(self, list_head):
        self.list_head = list_head

    def __next__(self):
        if not self.list_head:
            raise StopIteration()
        tmp_value = self.list_head
        self.list_head = self.list_head.next
        return tmp_value


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        return SingleLinkedListGenerator(self.head)

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
        elif self.head == remove:
            self.head = None
        else:
            itr = self.head
            while (itr.next):
                if itr.next == remove:
                    itr.next = itr.next.next
                print(itr)
                itr = itr.next

    def __len__(self):
        if self.head is None:
            return 0
        else:
            itr = self.head
            count = 1
            while (itr.next):
                count += 1
                itr = itr.next
            return count


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
