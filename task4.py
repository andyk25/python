mlist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unlist = [elm for elm in mlist if mlist.count(elm) < 2]
print(*unlist)
