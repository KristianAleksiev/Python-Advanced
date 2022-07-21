def get_primary_diagonal_sum(matrix):
    the_sum = 0
    n = len(matrix)
    # for r in range(n):
    #     for c in range(n):
    #         if r == c:
    #             the_sum += matrix[r][c]
    for i in range(n):
        the_sum += matrix[i][i]
    return the_sum

n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

print(get_primary_diagonal_sum(matrix))
