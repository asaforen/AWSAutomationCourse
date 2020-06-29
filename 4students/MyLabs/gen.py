def myrange(start,stop):
    while start < stop:
        yield start
        start +=1

for x in myrange(10,20):
    print(x)