rows_count, columns_count = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])

columns_sums = [0] * columns_count

for row_index in range(rows_count):

    for column_index in range(columns_count):
        columns_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in columns_sums]


# def columns_sums(matrix):
#     columns_sums = [0] * columns_count
#
#     for row_index in range(rows_count):
#
#         for column_index in range(columns_count):
#             columns_sums[column_index] += matrix[row_index][column_index]
#
#     return columns_sums


# Second version of looping

# column_sums = []
# for column_index in range(columns_count):
#     column_sums.append(0)
#     for row_index in range(rows_count):
#         column_sums[-1] += matrix[row_index][column_index]
