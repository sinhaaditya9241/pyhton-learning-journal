# syntax

# class(name):
#     def __init__(self, parameters):
#         # initialization code here

# call the class
# statement 

# example:1
'''
class car:
    pass

car_1 = car()
print(car_1)
'''

# example:2
'''
class car:
    color = "black"

car_1 = car()
print(car_1.color)  # prints: black
'''
# example:3

class car:
    color = "black"
    type = "SUV"

car_1 = car()
print(car_1.color.upper()) # prints: BLACK
# ----> dot notation is used to access class attributes
print(car_1.type)   # prints: SUV