# урок 3 задача 4
def my_func1(x, y):
    return x ** y

def my_func2(x, y):
    poww = 1
    for i in range(abs(y)):
        poww /= x
    return poww
