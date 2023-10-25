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
print(silnia(10))
#print(silnia(10.3))
#print(silnia(0))
#print(silnia("a"))

