values = [1, -1, 5, 3, 8, 4, 2]
"""
print(sorted(values))  # New, sorted collection
values.sort()  # sorts the current list
print(values)
"""

print(sorted([1, -1, 5, 3, 8, 4, 2]))
print(sorted(["Pesho", "Gosho", "Dimitar"]))

"""Tuples are sortable"""
print(sorted([(1, 7), (-1, 3), (1, 4)]))

print(sorted([1, -1, 5, 3, 8, 4, 2], reverse=True))
print(sorted([1, -5, 5, 3, 8, 4, 2], reverse=True, key=lambda x: x % 5))


def order_by_remainder_5(x):
    return x % 5


print(sorted([1, -5, 5, 3, 8, 4, 2], reverse=True, key=order_by_remainder_5))

print(sorted([1, -5, 5, 3, 8, 4, 2], reverse=True, key=lambda x: (x % 5, x)))
# Sort by remainder and by value -> AS A TUPLE


dd = {
    "Peter": 21,
    "George": 18,
    "John": 45
}
print(dd)
print(sorted(dd))  # Sorting the keys
print(sorted(dd.items()))
print(sorted(dd.items(), key=lambda x: x[1]))  # Sorted by values
