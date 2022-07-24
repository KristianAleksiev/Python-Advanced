# def f1():
#     def f2():
#         print("I am f2")
#     print("I am f1")
#     f2()
#
# f1()
# f2()

def math_operation(operation, *args):
    """Creating abstraction"""

    def add(*args):
        return sum(args)

    def subtract(*args):
        return sum(-x for x in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    if operation == "+":
        return add(*args)
    elif operation == "-":
        return subtract(*args)
    elif operation == "+":
        return multiply(*args)
    else:
        return None


print(math_operation("+", 1, 2, 3, 4))
print(math_operation("-", 1, 2, 3, 4))
print(math_operation("*", 1, 2, 3, 4))


def math_operation_factory(operation):
    def add(*args):
        return sum(args)

    def subtract(*args):
        return sum(-x for x in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    if operation == "+":
        return add
    elif operation == "-":
        return subtract
    elif operation == "+":
        return multiply
    else:
        return None


add = math_operation_factory("+")
print(add(1, 2, 3))
add2 = math_operation_factory("+")

print(add == add2)  # The inner functions are created in the memory every time we call the outer one

