# Function to calculate factorial using recursion

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Sample call to the function

sample_number = int(input('enter a number : '))
result = factorial(sample_number)

# Print the result

print(f"The factorial of {sample_number} is: {result}")
