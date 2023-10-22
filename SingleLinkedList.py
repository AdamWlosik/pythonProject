
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def clear(self):
        self.head = None

    def append(self, append):
        self.head = append

    def remove(self):
        pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



