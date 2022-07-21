def get_primary_diagonal_sum(matrix):
    """Sum of primary diagonal in N * N matrix"""
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))


def get_secondary_diagonal_sum(matrix):
    """Sum of secondary diagonal in N * N matrix"""
    n = len(matrix)
    return sum(matrix[i][n - i - 1] for i in range(n))
