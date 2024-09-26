# Sample string
str1 = "hello world"
str2 = "HELLO WORLD"
str3 = "  hello  "

# upper()
print("Uppercase: ", str1.upper())

# lower()
print("Lowercase: ", str2.lower())

#capitalize()
print("Capitalized: ", str1.capitalize())

# strip()
print("Stripped: '", str3.strip(), "'")

# replace()
print("Replaced: ", str1.replace("world", "Python"))

# split()
words = str1.split()
print("Split: ", words)

# join()
joined_str = '-'.join(words)
print("Joined: ", joined_str)

# find()
index = str1.find('world')
print("Index of : ", index)

#  startswith
print("Starts with : ", str1.startswith('hello'))

#isdigit()
print("Is digit: ", '12345'.isdigit())
print("Is digit: ", str1.isdigit())


'''

'''