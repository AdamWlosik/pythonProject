from SingleLinkedList import Node, SingleLinkedList


def silnia(n):
    silnia = 1
    if isinstance(n, int):
        if n == 0:
            return 1
        elif n < 0:
            raise ValueError("ujemna")
        else:
            for i in range(1, n + 1):
                silnia = silnia * i
                #print(silnia)
            return silnia
    else:
        raise TypeError("zły typ")


#print(silnia(1))
#print(silnia(-10))
#print(silnia(10))
#print(silnia(10.3))
#print(silnia(0))
#print(silnia("a"))

lista = [1, 2, 3]

for i in lista:
    print(i)
it = iter(lista)
print(type(it))
print(dir(it))
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

for i in lista_testowa:
    print(i.value)
