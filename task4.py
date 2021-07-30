# задача 4
# _*_ coding: utf8 # включить кодировку utf8


class Car:


    def __init__(self, speed=0, color="", name=""):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False


    def go(self):
        print("машина поехала")


    def stop(self):
        print("машина остановилась")


    def turn(self, direction):
        print(f"машина повернула {direction}")


    def show_speed(self):
        print(f"текущщая скорость {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили допустимую скорость")
        else:
            print(f"текущщая скорость {self.speed}")


class WorkCar(Car):


    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили допустимую скорость")
        else:
            print(f"текущщая скорость {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):


    def __init__(self, speed=0, color="", name=""):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = True


cars = []
cars.append(WorkCar(30, "красный", "лошадка"))
cars.append(TownCar(80, "синий", "блоха"))
cars.append(SportCar(150, "белый", "стриж"))
cars.append(PoliceCar(180, "черный", "носорог"))
for elm in cars:
    print(elm.name, elm.speed, elm.color, end=" ")
    print((" ", "Полицейская")[elm.is_police])
    elm.go()
    elm.show_speed()
    elm.stop()
    print()
