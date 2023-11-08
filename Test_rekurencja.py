import unittest

from rekurnecja import Rekurencja


class TestRekurencjaPodstawowa(unittest.TestCase):

    def test_rekurencja_dla_1(self):
        test = Rekurencja()
        self.assertEqual(1, test.mysum([1]))

    def test_rekurencja_lista(self):
        test = Rekurencja()
        self.assertEqual(15, test.mysum([1, 2, 3, 4, 5]))

    def test_rekurencja_lista_str(self):
        test = Rekurencja()
        self.assertEqual('jajko', test.mysum(('j', 'a', 'j', 'k', 'o')))

    def test_rekurencja_lista_wyrazow(self):
        test = Rekurencja()
        self.assertEqual('mielonkaszynkajajko', test.mysum(['mielonka', 'szynka', 'jajko']))


class TestRekurencjaRozszerzonePrzypisanie(unittest.TestCase):

    def test_rekurencja_dla_1(self):
        test = Rekurencja()
        self.assertEqual(1, test.mysum4([1]))

    def test_rekurencja_lista(self):
        test = Rekurencja()
        self.assertEqual(15, test.mysum4([1, 2, 3, 4, 5]))

    def test_rekurencja_lista_str(self):
        test = Rekurencja()
        self.assertEqual('jajko', test.mysum4(('j', 'a', 'j', 'k', 'o')))

    def test_rekurencja_lista_wyrazow(self):
        test = Rekurencja()
        self.assertEqual('mielonkaszynkajajko', test.mysum4(['mielonka', 'szynka', 'jajko']))
