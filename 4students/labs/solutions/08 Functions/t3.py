def f1():
    yield 2
    yield 1
    yield 7
    yield 4


for num in f1():
    print(num)
