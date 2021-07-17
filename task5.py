# урок 4 задача 5
import functools as ft


def pr(x, y):
    return x*y


numbers = [i for i in range(100, 1001, 2)]

print(ft.reduce(pr, numbers))
