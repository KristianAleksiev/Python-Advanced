tt = (
    [1, 2, 3],
    {},
    (4, 5, 6)
)

print(tt)

tt[0].append(-5)
print(tt)

tt[1]["one"] = 1
print(tt)

# The starting tuple still consists of a list, dictionary and tuple
# The object inside the tuples can be changed if the object is mutable
