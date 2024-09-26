tup1= ('amar', 12, 'prem', 2, 'atharv', 3.3, 'samii')
tup2 = ('radhey', 20, 0.9, 'OmBahnuse', 'omraut', 'Yash')

# count()
print("Count : ", tup1.count('amar'))

# index()

print("Index of 'prem': ", tup1.index('prem'))


# Converting tup1 to list for modification
list1 = list(tup1)
# append()
list1.append(34)
tup1= tuple(list1)
print("Appended tuple: ", tup1)

# extend()
list1 = list(tup1)
list1.extend(tup2)
tup1= tuple(list1)
print("Extended tuple: ", tup1)

# insert()

list1 = list(tup1)
list1.insert(2, 'newmember')
tup1= tuple(list1)
print("After inserting : ", tup1)

# reverse()
list1 = list(tup1)
list1.reverse()
tup1= tuple(list1)
print("Reversed tuple: ", tup1)

# remove()
list1 = list(tup1)
list1.remove('prem')
tup1= tuple(list1)
print("After removing 'prem': ", tup1)

# sort()
list2 = list(tup2)
list2 = ['radhey', 'omraut', 'Yash', 'OmBahnuse']
list2.sort()
tup2 = tuple(list2)
print("Sorted tup2: ", tup2)

# pop()
list1 = list(tup1)
popped_element = list1.pop()
tup1= tuple(list1)
print("Popped element: ", popped_element)
print("After popping: ", tup1)
