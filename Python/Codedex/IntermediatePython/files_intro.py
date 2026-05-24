# This opens example file for writing
file = open('example.txt', 'w')

# This writes a line to the file
file.write('Hello, World! 🌎')

# This closes the file
file.close()

# This opens the same file for reading
file = open('example.txt', 'r')

# This reads the content of the file and prints it
content = file.read()
print(content)

# This closes the file
file.close()

# This opens the file again for appending
file = open('example.txt', 'a')

# This writes another line to the file
file.write('\nThis is an additional line.')

# This closes the file
file.close()

#'w' mode will overwrite the existing file, while 'a' mode will append to it.