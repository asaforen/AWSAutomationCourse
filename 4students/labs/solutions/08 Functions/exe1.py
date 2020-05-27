import math
list1 = [-2,4,5,-5,10,20,-50]

list2 = list(map(math.sin, filter(lambda x: x > 0, list1)))
list3 = [math.sin(x) for x in list1 if x > 0]
print(list2,type(list2))
print(list3, type(list3))