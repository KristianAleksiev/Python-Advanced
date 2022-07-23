sublists = input().split("|")

result = []

for index in range(len(sublists) - 1, -1, -1):
    current_sub = sublists[index].strip().split()
    result.extend(current_sub)

print(*result, sep=" ")


"""
matrix = [
    [7, 1, 3],
    [1, 3, 9],
    [4, 6, 7, 0]
]
print(sum(matrix, [])) -> [7, 1, 3, 1, 3, 9, 4, 6, 7, 0]
"""