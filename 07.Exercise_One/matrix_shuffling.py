def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()

    if line == "END":
        break

    line_parts = line.split()

    if len(line_parts) != 5 or line_parts[0] != "swap":
        print("Invalid input!")
        continue

    row_one, col_one, row_two, col_two = [int(x) for x in line_parts[1:]]

    if is_outside(row_one, col_one, rows, cols) or is_outside(row_two, col_two, rows, cols):
        print("Invalid input!")
        continue

    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]

    for row in matrix:
        print(*row, sep=" ")
