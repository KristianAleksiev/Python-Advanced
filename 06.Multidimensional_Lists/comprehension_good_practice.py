matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
]


# print([[x for x in row if x % 2 == 0] for row in matrix])


def is_even(number):
    return number % 2 == 0


def remove_odd_numbers(list_param):
    return [x for x in list_param if is_even(x)]


print([remove_odd_numbers(row) for row in matrix])
