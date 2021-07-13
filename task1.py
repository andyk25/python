# урок 3 задача 1
def div(x,y):
    return ("на ноль делить нельзя" if y == 0 else x / y)
# 
dx = float(input("Веедите делимое : "))
dy = float(input("Введите делитель : "))
print (div(dx,dy))