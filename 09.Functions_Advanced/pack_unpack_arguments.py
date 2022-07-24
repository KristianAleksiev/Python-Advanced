def f(*args, **kwargs):
    print(f"Args w/o * {args}")
    print(*args)
    print(**kwargs)
    return sum(args)


print(f(1, a=2))

ll = [1, 2, 3, 4]

k, l, *r = ll  # Get first two values, the other left in the list put in a new list in r

# k, l*, r = ll
# k, *_, r = ll #  Need the first and the last element, don't need the other values between them


print(k)
print(l)
print(r)

#######################################################
"""
ll1 = [1, 2, 3, 4]

k, l, *r = ll1
print(k, l, r)

ll2 = [-1, *ll1, -2]  # [-1, 1, 2, 3, 4, -2]
print(ll2)

dd1 = {"x": 1, "y": 2}

dd2 = {"z": 3,
       **dd1,
}

print(dd2)

"""

numbers = [1, 2, 3, 4, 5]
grades_dict = {
    "Georgi": 3,
    "Ivan": 4,
    "Maria": 6,
    "Pesho": 4.5
}


def n(*args, **kwargs):
    print(f"args={args}, kwargs={kwargs}")


f(*numbers)  # 5 arg - tuple of unpacked elements from the list
f(numbers)  # 1 arg - the list
f(**grades_dict)
f(*numbers, **grades_dict)


def congrat(Maria, **kwargs):
    print(f"Maria has {Maria}. She is smart!")


congrat(**grades_dict)
#  KEY OF THE DICT MATCHES THE NAMES OF THE PARAMS
