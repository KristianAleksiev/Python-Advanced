rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

flatten = [number for row in matrix for number in row]

print(flatten)