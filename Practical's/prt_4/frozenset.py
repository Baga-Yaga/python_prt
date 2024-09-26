
frozenset1 = frozenset([1, 2, 3, 4, 5])
frozenset2 = frozenset([4, 5, 6, 7, 8])

# union()
union_fs = frozenset1.union(frozenset2)
print("Union : ", union_fs)

# intersection()
intersection_fs = frozenset1.intersection(frozenset2)
print("Intersection : ", intersection_fs)

# difference()
difference_fs = frozenset1.difference(frozenset2)
print("Difference : ", difference_fs)

# symmetric_difference()
symmetric_difference_fs = frozenset1.symmetric_difference(frozenset2)
print("Symmetric difference : ", symmetric_difference_fs)

# issubset()
is_subset = frozenset1.issubset(frozenset2)
print("Is frozenset1 a subset of frozenset2? ", is_subset)

# issuperset()
is_superset = frozenset1.issuperset(frozenset2)
print("Is frozenset1 a superset of frozenset2? ", is_superset)

# isdisjoint()
is_disjoint = frozenset1.isdisjoint(frozenset2)
print("Are frozenset1 and frozenset2 disjoint? ", is_disjoint)

# copy()
frozenset_copy = frozenset1.copy()
print("Copy: ", frozenset_copy)

# len()
length = len(frozenset1)
print("Length : ", length)

# in
is_in = 3 in frozenset1
print("Is 3 in frozenset1? ", is_in)
