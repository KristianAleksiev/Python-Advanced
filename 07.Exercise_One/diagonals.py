size = int(input())

matrix = []
primary = []
secondary = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

sum_primary = sum(primary)
sum_secondary = sum(secondary)

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum_secondary}")
