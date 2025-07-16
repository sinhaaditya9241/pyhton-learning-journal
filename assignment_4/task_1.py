# task1_read_file.py

try:
    # Open the file in read mode
    file1 = open('sample.txt', 'r') 

    # Read the content of the file
    reading_file = file1.read() 

    # Print the content of the file
    print("File content:")
    print(reading_file) 

    # Close the file
    file1.close() 

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
