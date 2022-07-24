def f1(x):
    def inner_f1(y):
        return x + y

    return inner_f1


func1 = f1(5)
print(func1(6))
print(func1(5))
func2 = f1(-5)
print(func2(6))
print(func2(5))
"""
The inner func could tap into the parent's parameters
Saving state of a function
"""
