from itertools import count

for i in count(3):
    if i > 20:
        break
    else:
        print(i, end=' ')
