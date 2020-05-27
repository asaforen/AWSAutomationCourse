def myFilter(x):
    return x<0


names =['ds','Asds','fd','dsds','dsdsd']


l1 = [5,4,-6,1,2,-3]


iter5 = map(lambda x:x*10, filter(lambda x:x>=0,l1))
print(list(iter5))

list6 = (x*10 for x in l1 if x>=0)
print(list(list6))

iter2 = filter(lambda x:x>=0,l1)
iter3 = filter(myFilter,l1)
iter31 = map(myFilter,l1)


iter4 = filter(lambda x:len(x)>3,names)
#print(list(iter2))
print(list(iter3))
print(list(iter31))
#print(list(iter4))

