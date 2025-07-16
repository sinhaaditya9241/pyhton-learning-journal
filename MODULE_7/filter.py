# filter
# filter (function , iterable)


def even(a):
    return a % 2 == 0

number = range(1,51) # 1 to 50

ans = set(filter(lambda a : a % 2 == 0, number))

print(ans )