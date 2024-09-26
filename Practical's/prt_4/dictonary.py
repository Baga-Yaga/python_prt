
dict1 = {'name': 'Amar',
         'age': 25,
         'city': 'Mumbai'}
dict2 = {'country': 'India',
         'language': 'Hindi'}

# clear()
dict_copy = dict1.copy()
dict_copy.clear()
print("Cleared dictionary: ", dict_copy)

# copy()
dict_copy = dict1.copy()
print("Copied dictionary: ", dict_copy)

# get()
age = dict1.get('age')
print("Age: ", age)

# pop()
city = dict1.pop('city')
print("Popped 'city': ", city)
print("Dictionary after pop: ", dict1)

# popitem()
last_item = dict1.popitem()
print("Popped item: ", last_item)
print("Dictionary after : ", dict1)

# keys()
print("Keys in dict1: ", dict1.keys())

# values()
print("Values in dict1: ", dict1.values())

# items()
print("Items in dict1: ", dict1.items())

# update()
dict1.update(dict2)
print("Updated dict1 with dict2: ", dict1)

# setdefault()
country = dict1.setdefault('country', 'Unknown')
print("Country (using setdefault): ", country)
print("Dictionary after setdefault: ", dict1)

# Fromkeys()
new_dict = dict.fromkeys(['name', 'age', 'city'], 'Unknown')
print("New dictionary from keys: ", new_dict)



'''
Method 	        Description

clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	         Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	         Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''
