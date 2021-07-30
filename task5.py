# задача 5
# _*_ coding: utf8 # включить кодировку utf8


class Stationery:


    def __init__(self, title):
        self.title = title


    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):


    def draw(self):
        print("Рисуем ручкой.")


class Pencil(Stationery):


    def draw(self):
        print("Рисуем карандашом.")


class Handle(Stationery):


    def draw(self):
        print("Рисуем маркером.")


markers = []
markers.append(Stationery("лошадка"))
markers.append(Pen("блоха"))
markers.append(Pencil("стриж"))
markers.append(Handle("бегемот"))
for elm in markers:
    elm.draw()
