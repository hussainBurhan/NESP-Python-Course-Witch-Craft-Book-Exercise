# Opening a file named 'Test_text.txt' in read mode
with open('Test_text.txt', 'r') as file:
    # Reading all lines from the file into a list
    lines_list = file.readlines()

# Printing the list of lines
print('Creating a list of lines: ')
print(lines_list)

# Separator for output clarity
print('x'*50)

# Reversing and printing lines in reverse order
print('Reverse the order of lines: ')
for line in lines_list[::-1]:
    print(line, end = '')

# Separator for output clarity
print('x'*50)

# Displaying all characters in the file
print('Displaying all characters : ')
with open('Test_text.txt', 'r') as file:
    characters = file.read()
    print(characters)

# Separator for output clarity
print('x'*50)

# Displaying all characters in reverse order
print('Displaying all characters in reverse order ')
for char in characters[::-1]:
    print(char, end = '')
