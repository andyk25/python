# задача 2
# _*_ coding: utf8 # включить кодировку utf8

class Road:

    __tn = 10  # толшина асфальта
    __dn = 10  # вес афальта 1 кв метра толщиной 1см


    def __init__(self, leng=1, width=1):
        self._leng = leng
        self._width = width


    def mass_asph(self):
        return self._leng * self._width * Road.__tn * Road.__dn


ln, wd = map(int, input(
    "введите длину и ширину асфальта (метры)чз пробел :").split())

rd = Road(ln, wd)
print(f"масса афальта необходимого для дороги = {rd.mass_asph()} кг")
