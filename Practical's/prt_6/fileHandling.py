sample_text = "Hello, world!\nWelcome to Python file handling."

# open()
file = open("sample.txt", "w")
file.write(sample_text)  # Write some text to the file
file.close()

# read()
file = open("sample.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()

# readline()
file = open("sample.txt", "r")
first_line = file.readline()
print("First line: ", first_line)
file.close()

# readlines()
file = open("sample.txt", "r")
all_lines = file.readlines()
print("All lines: ", all_lines)
file.close()

# 5. write() - Writes a string to a file
file = open("sample.txt", "a")  # Open in append mode
file.write("\nAdding another line.")
file.close()

# writelines()
file = open("sample.txt", "a")
lines = ["\nMy Names BabaYaga", "\nMy names John Wick"]
file.writelines(lines)
file.close()

# append()
file = open("sample.txt", "a")
file.write("\nJohn is a man of focus!")
file.close()

# tell()
file = open("sample.txt", "r")
file.read(5)
position = file.tell()
print("Current pointer position: ", position)
file.close()

# seek()
file = open("sample.txt", "r")
file.seek(0)
print("After seeking: ", file.read(10))
file.close()

# close()
file = open("sample.txt", "r")
print("Is file closed? ", file.closed)
file.close()
print("Is file closed now? ", file.closed)

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content :\n", content)
