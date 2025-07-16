# Python Basics – Conditional Statements and Loops

This repository contains two beginner-level Python tasks to practice **conditional statements** and **loops**.

---

##  Task 1: Check if a Number is Even or Odd

###  Problem Statement

Write a Python program that:

1. Accepts an integer input from the user.
2. Determines whether the number is even or odd.
3. Displays the result.

###  Approach

- Use `input()` to get user input and convert it to an integer.
- Use the modulus operator `%` to check if the number is divisible by 2.
- Print "even" if divisible by 2; otherwise, print "odd".

###  Code

```python
a = int(input('Enter a number: '))
if a % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')


# Task 2: Sum of Integers from 1 to 50 Using a Loop

## Problem Statement

Write a Python program that:

1. Uses a `for` loop to iterate over numbers from 1 to 50.  
2. Calculates the sum of all integers in this range.  
3. Displays the final sum.

---

##  Approach

- Initialize a variable `total_sum` to store the sum.
- Use a `for` loop to iterate from 1 to 50 using `range(1, 51)`.
- In each iteration, add the current number to `total_sum`.
- Print the final value of `total_sum` after the loop ends.

---

##  Code

```python
# Initialize sum to 0
total_sum = 0

# Loop through numbers from 1 to 50
for number in range(1, 51):
    total_sum += number  # Add each number to the total sum

# Display the result
print("The sum of integers from 1 to 50 is:", total_sum)
