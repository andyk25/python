mylist = []
mylist.append('a')
mylist.append(5)
mylist.append(3.5)
mylist.append(b'46')
mylist.append(False)
mylist.append(complex(3, 5))
mylist.append((3, 5, 6, 7))
mylist.append([33, 55, 16, 8])
mylist.append({34, 55, 66, 87})
for i in mylist:
    print(type(i))
