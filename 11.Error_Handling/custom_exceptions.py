class ValueTooSmallException(Exception):
    pass


value = int(input())

if value < 10:
    raise ValueTooSmallException(f"{value} should be equal or greater than 15")

"""
Custom Exception is implemented through inheritance
"""

str_value = input()
for x in str_value:
    if x not in ["0", "1"]:
        raise ValueError("The input should contain only '0's and '1's")

value = int(str_value)
