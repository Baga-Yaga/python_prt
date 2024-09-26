# Sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# add()
set1.add(6)
print("After adding : ", set1)

# remove()
set1.remove(6)
print("After removing: ", set1)

# discard()
set1.discard(5)
print("After discarding: ", set1)

# union()
union_set = set1.union(set2)
print("Union : ", union_set)

# intersection()
intersection_set = set1.intersection(set2)
print("Intersection : ", intersection_set)

# difference()
difference_set = set1.difference(set2)
print("Difference : ", difference_set)

# symmetric_difference()
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2: ", symmetric_difference_set)

# issubset()
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2? ", is_subset)

# issuperset()
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2? ", is_superset)

# clear()
set1.clear()
print("After clearing set1: ", set1)
