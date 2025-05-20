# iterator
'''
list = range (1,10)

for i in list:
    print(i)

iteration = (iter(list))
print(iteration.__next__(1))
print(iteration.__next__(2))

'''

# generator

def fn():

    yield 1
    yield 2
    yield 3
    

value = fn()
print(value.__next__())
print(value.__next__())
print(value.__next__())

for i in fn():
    print(i)



def square():

    n = 1
    while n <= 5:
        square = n ** 2
        yield square
        n = n + 1

value = square()
for i in value:
    print(i)