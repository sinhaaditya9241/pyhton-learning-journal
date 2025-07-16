# map
# map (function, iterable)

number = range(1,6)

def square(x):
    return x**2

ans = list(map(square, number))

print(ans)


def square(x):
    return x**2

ans = list(filter(square, number))

print(ans)


def square(x):
    return x% 2 == 0

ans = list(map(square, number))

print(ans)

def square(x):
    return x% 2 == 0

ans = list(map(lambda a: a ** 2 , number))

print(ans)