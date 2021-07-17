from itertools import cycle

mylist = [1, 2, 3]
i = 1
for elm in cycle(mylist):
    if i > 20:
        break
    else:
        print(elm, end=' ')
    i += 1
