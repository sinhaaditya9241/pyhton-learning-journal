# tuple 

number = (1, 2, 3, 4, 5)

print(number) 

tup1 = ('mike', 10 , 2 , 5)
tup2 = ('john', 20 , 3 , 6)
print(tup1+tup2)


tup = (1, 'mike' , 2 , 5)
print(len(tup))


# tuple ----> imutable
# list ---->  mutable
'''
number = (1, 2, 3, 4, 5)
number[0] = 0
print(number)
# output: (0, 2, 3, 4, 5)  
'''
tup = (1, 2, 3, 4, 5)
tup_sort = sorted(tup)
print(tup_sort)  # output: [1, 2, 3, 4

tup_index = tup.index(4)
print(tup_index)