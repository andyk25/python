# задача 2
# _*_ coding: utf8 # включить кодировку utf8
from abc import ABC, abstractmethod


class Clothes_abc(ABC):


    @abstractmethod
    def add_coat(self, V):
        pass


    @abstractmethod
    def add_costume(self, H):
        pass


class Coat_abc(ABC):
    pass


class Costume_abc(ABC):
    pass


class Coat(Coat_abc):


    def __init__(self, V):
        self.V = V
        self.square = V/6.5 + 0.5


class Costume(Costume_abc):

    def __init__(self, H):
        self.H = H
        self.square = 2 * H + 0.3


class Clothes(Clothes_abc):


    def __init__(self):
        self.units = []


    def add_coat(self, V):
        self.units.append(Coat(V))

    def add_costume(self, H):
        self.units.append(Costume(H))


    @property
    def square(self):
        square = 0
        for el in self.units:
            square += el.square
        return square


cl = Clothes()
print("Одежды нет, расход ткани : ", cl.square)
cl.add_coat(10)
cl.add_coat(20)
cl.add_coat(40)
cl.add_costume(10)
cl.add_costume(20)
cl.add_costume(15)
print("Добавили одежду, расход ткани : ", cl.square)
