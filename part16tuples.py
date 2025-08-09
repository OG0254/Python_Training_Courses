tup1 = (1,2,3,5)
l1 = list(tup1) #unpacking
l1[3] = 4
tup1 = tuple(l1) #packing  you have to do this two processes since you can't edit a tuple
print(tup1)