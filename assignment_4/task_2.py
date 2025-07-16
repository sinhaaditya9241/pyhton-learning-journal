# task2_write_append_file.py

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data + '\n')

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_file(filename):
    with open(filename, 'r') as file:
        print("Final content of the file:")
        for line in file:
            print(line.strip())

# Taking input from user
user_input = input("Enter a number or text to write into the file: ")

# File name
filename = "output.txt"

# Write and append
write_to_file(filename, user_input)
append_to_file(filename, "This is the appended line.")

# Display file contents
read_file(filename)
