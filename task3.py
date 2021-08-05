# задача 3
# _*_ coding: utf8 # включить кодировку utf8

class Cell:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        sub = self.num - other.num
        if sub > 0:
            return Cell(sub)
        else:
            print("вычитание невозможно")

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        if other.num == 0:
            print("деление невозможно")
        else:
            return Cell((round(self.num / other.num)))

    def make_order(self, num):
        diff = self.num - num * int(self.num/num)
        str_cell = ""
        for i in range(int(self.num/num)):
            str_cell += "*" * num + "\n"
        str_cell += "*" * diff + "\n"
        return str_cell

cl1 = Cell(20)
cl2 = Cell(10)
razn = cl1 - cl2
addic = cl1 + cl2
multy = cl1 * cl2
diff = cl1 / cl2
print(razn.num)
print(addic.num)
print(multy.num)
print(diff.num)
print(multy.make_order(49))
