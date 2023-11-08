class Rekurencja:
    # rekurencja podstawowa
    def mysum(self, L):
        if not L:
            # print(L)
            return 0
        else:
            return L[0] + self.mysum(L[1:])

    # print(mysum([1, 2, 3, 4, 5]))

    # trójskładniowa operacja if/else
    def mysum2(self, L):
        return 0 if not L else L[0] + self.mysum2(L[1:])

    # dowolny typ domyślnie wartość 1
    def mysum3(self, L):
        return L[0] if len(L) == 1 else L[0] + self.mysum3(L[1:])

    # rozszerzone przypisane

    def mysum4(self, L):
        first, *rest = L
        return first if not rest else first + self.mysum4(rest)

    # rekurencja pośrednia
    def mysum5(self, L):
        if not L:
            return 0
        return self.notempyt(L)

    def notempyt(self, L):
        return L[0] + self.mysum5(L[1:])


test = Rekurencja()
print(test.mysum([1]))
print(test.mysum2([1]))
print(test.mysum3([1]))
print(test.mysum4([1]))

print(test.mysum([1, 2, 3, 4, 5]))
print(test.mysum2([1, 2, 3, 4, 5]))
print(test.mysum3([1, 2, 3, 4, 5]))
print(test.mysum4([1, 2, 3, 4, 5]))

# print(test.mysum(('j', 'a', 'j', 'k', 'o')))
# print(test.mysum2(('j', 'a', 'j', 'k', 'o')))
print(test.mysum3(('j', 'a', 'j', 'k', 'o')))
print(test.mysum4(('j', 'a', 'j', 'k', 'o')))

# print(test.mysum(['mielonka', 'szynka', 'jajko']))
# print(test.mysum2(['mielonka', 'szynka', 'jajko']))
print(test.mysum3(['mielonka', 'szynka', 'jajko']))
print(test.mysum4(['mielonka', 'szynka', 'jajko']))

print(test.mysum5([1]))
print(test.mysum5([1, 2, 3, 4, 5]))
# print(test.mysum5(('j', 'a', 'j', 'k', 'o')))
# print(test.mysum5(['mielonka', 'szynka', 'jajko']))
