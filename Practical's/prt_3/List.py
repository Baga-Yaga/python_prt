list1 = ['amar', 12, 'prem', 2,'atharv',3.3 ,'samii']
list2 = ['radhey', 20, 0.9, 'OmBahnuse' , 'omraut', 'Yash']

# append()
list1.append(34)
print("Appended : " ,list1)

# copy()
list3 = []
list3 = list2.copy()
print("Copied List : ", list3)

# count()
print("Count of 'amar': ", list1.count('amar'))

# extend()
list1.extend(list2)
print("Extended list1 : ", list1)

# index()
print("Index of 'prem': ", list1.index('prem'))

list1.insert(2, 'newmember')
print("After inserting at index 2: ", list1)

# reverse()
list1.reverse()
print("Reversed list1: ", list1)

# remove()
list1.remove('prem')
print("After removing 'prem': ", list1)

list3 = ['radhey', 'omraut', 'Yash', 'OmBahnuse']
list3.sort()
print("Sorted list3: ", list3)

# pop()
pop_ele = list1.pop()
print("Popped element: ", pop_ele)
print("After popping: ", list1)


#clear()
print("Cleared List : ",list1.clear())


'''
inbuilt function for lists in python 

Method 	    Description

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

'''