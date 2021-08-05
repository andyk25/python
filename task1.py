# задача 1
# _*_ coding: utf8 # включить кодировку utf8

class Matrix:


    def __init__(self, mx):
        self.mx = mx


# вывод матрицы столбиком
    def __str__(self):
        mx_out = ""
        for line in self.mx:
            mx_out += f"{' '.join(map(str,line))} \n"
        return mx_out


# Сложение матриц
    def __add__(self, other):
        sm = []
        for ln1, ln2 in zip(self.mx, other.mx):
            line = []
            for elm1, elm2 in zip(ln1, ln2):
                line.append(elm1+elm2)
            sm.append(line)
        return Matrix(sm)


mx1 = Matrix([[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 3, 2], [3, 1, 1, 3]])
mx2 = Matrix([[4, 3, 2, 4], [1, 3, 3, 1], [2, 3, 3, 2], [3, 1, 1, 3]])
mx3 = mx1+mx2
print(mx1, mx2, mx3, sep="\n")
