mylist = []
elm = '1'
while elm != '':
    elm = input("введите элемент списка : ")
    mylist.append(elm)
mylist.pop()
print(*mylist)
for i in range(0, len(mylist) // 2 * 2, 2):
    mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
print(*mylist)
