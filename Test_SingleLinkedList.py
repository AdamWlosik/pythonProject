import unittest

from SingleLinkedList import SingleLinkedList, Node


class TestSingleLinkedList(unittest.TestCase):

    def test_clear_empty_list_expected_empty_list(self):
        # arrange
        lista_testowa = SingleLinkedList()
        # act
        lista_testowa.clear()
        # assert
        self.assertEqual(None, lista_testowa.head)

    def test_append(self):
        lista_testowa = SingleLinkedList()
        test = 1
        lista_testowa.append(test)
        self.assertEqual(test, lista_testowa.head.value)

    def test_not_empty(self):
        # arrange
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        lista_testowa = SingleLinkedList()
        lista_testowa.head = node1
        node1.next = node2
        node2.next = node3
        # act
        test = 10
        lista_testowa.append(test)
        # assert
        self.assertEqual(test, node3.next.value)


if __name__ == '__main__':
    unittest.main()

# test dla append
