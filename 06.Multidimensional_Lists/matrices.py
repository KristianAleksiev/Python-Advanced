# Matrix - Even number of columns for each row
# On Main diagonal -> row_index == column_index
# On Secondary diagonal -> row_index == n(number of rows and cols) - column_index - 1


l_of_zeros = []
n = 5
m = 7
for _ in range(5):
    l_of_zeros.append(0)

# matrix of N*M
mm = []
for _ in range(n):
    ll = []
    for _ in range(m):
        ll.append(0)

    mm.append(ll)

print(mm)


# Matrix template
def read_matrix():
    n, m = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = read_matrix()

# Comprehensions

# Nested
comprehended_m = [[v + 1 for v in row] for row in mm]

# Flat the matrix - MD comprehension
one_dim_list = [v + 1 for row in mm for v in row]


matrix_two = [[int(x) for x in input().split(", ")] for _ in range(n)]