'''
name = input("enter your name: ")
number = len(name) * 3 
print("hello {}, your lucky number is {}".format(name, number))
'''

example = "format() method "
string = "this is a example of {} on a string".format(example)
print(string)  # Output: this is a example of example of  on a string

first = "apple"
second = "banana"
print("I love to eat {0} and {1}".format(first, second))  

price = 150
with_tax = 150 +50
print(price, with_tax)  # Output: 150 200

print("price is {0} and with tax is {1}".format(price, with_tax))

print("price: Rs{:,2f}, with_tax: Rs{:,2f}".format(price, with_tax))