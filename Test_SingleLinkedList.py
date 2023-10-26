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

    def test_append_empty_list(self):
        lista_testowa = SingleLinkedList()
        test = 1
        lista_testowa.append(test)
        self.assertEqual(test, lista_testowa.head.value)

    def test_append_not_empty(self):
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

    def test_remove_empty_list(self):
        lista_testowa = SingleLinkedList()
        with self.assertRaises(ValueError):
            lista_testowa.remove(5)

    def test_remove_one_element_list_expected_empty_list(self):
        lista_testowa = SingleLinkedList()
        node = Node(1)
        lista_testowa.head = node
        lista_testowa.remove(node)
        self.assertEqual(None, lista_testowa.head)

    # przetestować gdy lista ma 5 elementów i żaden nie jest do usunięcia, na później

    def test_remove_center_element_expected_element_remove(self):
        lista_testowa = SingleLinkedList()
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
        self.assertEqual(node2.next, node4)

    def test_len_expected_list_length(self):
        lista_testowa = SingleLinkedList()
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
        test = 5
        lista_testowa.len()
        self.assertEqual(test, lista_testowa.len())


if __name__ == '__main__':
    unittest.main()

# kontekst protokół iteratora
# len
# remove test
