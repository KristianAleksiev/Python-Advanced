# Definition - Unique sequence, UNORDERED collection
# Sets are mutable
# Very fast search, add and remove operations

set_example = {1, 2, 3, 4, 5}
sett = {} #  -> Not set, dict
empty_set = set()

# Operators
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {1, 3, 4, 5}

print(s1.union(s2))
print(s2.intersection(s3))
print(s2.issubset(s3))
print(s1.difference(s2))
# Every set is a subset of itself

# Methods

[empty_set.add(1) for _ in range(100)]
print(empty_set)

set_example.remove(4)
print(4 in set_example)

set_example.add(4)
print(4 in set_example)

print(len(set_example))

# Set comprehensions
unique_nums = {int(num) for num in input().split()}