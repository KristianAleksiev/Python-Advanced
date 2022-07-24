def multiply(*args):
    result = 1
    for v in args:
        result *= v
    return result


print(multiply(1))
print(multiply(1, 2))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))