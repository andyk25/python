def fact(n):
    fc = 1
    for i in range(1, n+1):
        fc *= i
        yield fc


for el in fact(5):
    print(el)
