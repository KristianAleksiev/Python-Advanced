def get_next_position(row, col, direction):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_around_kids(matrix, row, col):
    result = []

    #  Left
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == "X" or matrix[row][col - 1] == "V":
        result.append([row, col - 1])

    #  Right
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == "X" or matrix[row][col + 1] == "V":
        result.append([row, col + 1])

    #  Up
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == "X" or matrix[row - 1][col] == "V":
        result.append([row - 1, col])

    #  Down
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == "X" or matrix[row + 1][col] == "V":
        result.append([row + 1, col])

    return result


gifts = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):

        if row_elements[col] == "S":
            santa_row, santa_col = row, col
        elif row_elements[col] == "V":
            nice_kids += 1

    matrix.append(row_elements)

nice_kids_presents = 0


while gifts > 0:
    line = input()
    if line == "Christmas morning":
        break

    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = get_next_position(santa_row, santa_col, line)

    if matrix[santa_row][santa_col] == "V":
        gifts -= 1
        nice_kids_presents += 1

    elif matrix[santa_row][santa_col] == "C":
        kids_around = get_around_kids(matrix, santa_row, santa_col)

        for kid_row, kid_col in kids_around:
            if matrix[kid_row][kid_col] == "V":
                nice_kids_presents += 1

            gifts -= 1
            matrix[kid_row][kid_col] = "-"

            if gifts == 0:
                break

    matrix[santa_row][santa_col] = "S"

if nice_kids_presents != nice_kids and gifts == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if nice_kids_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_presents} nice kid/s.")