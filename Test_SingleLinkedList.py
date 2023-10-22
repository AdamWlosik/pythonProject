import unittest

from SingleLinkedList import SingleLinkedList


class TestSingleLinkedList(unittest.TestCase):

    def test_clear_empty_list_expected_empty_list(self):
        # arrange
        lista_testowa = SingleLinkedList()
        # act
        lista_testowa.clear()
        # assert
        self.assertEqual(None, lista_testowa.head)

    def test_not_empty_list(self):
        lista_testowa = SingleLinkedList()
        test = 1
        lista_testowa.append(test)
        self.assertEqual(test, lista_testowa.head)

# test dla nie pusta lista
# test dla append
