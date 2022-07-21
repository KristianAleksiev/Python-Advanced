mm = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


print(mm[1][1])


# Looping -> Accessing elements by index
for row_index in range(len(mm)):
    for column_index in range(len(mm[0])):
        print(mm[row_index][column_index], end=" ")

