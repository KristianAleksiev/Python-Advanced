# Definition - Linear data structure, immutable(lists)
# Objects inside the tuples are mutable
# Only immutable methods apply to tuples
tt = (1, 2, 3, 4)
print(tt)
tt = (1, 2, 3)
print(tt)
print(tt[0])

tt2 = 1, 2, 3, 4, 5  # Also viable syntax
# Single element tuple
tt_1 = (1,)
n = 15
t_n = tuple(range(n))
print(t_n)

# Usage
# Methods

numbers = (1, 2, 1, 3, 1)
print(numbers.count(1))
print(numbers.index(2))
print(numbers.index(1, 1))  # Index of "1" right of index 1

print(1 in numbers)

# Loops
for value in numbers:
    print(value)

# Comprehension, not for tuples
[print(x) for x in numbers]

print(len(tt))

# Concatenation
print((1, 2) + (3, 4, 5))

# Unpacking
tuple_demo = (1, 2, 3)
x, y, z = tuple
print(x)
print(y)
print(z)

for (index, value) in enumerate(numbers):
    print(index)
    print(value)


