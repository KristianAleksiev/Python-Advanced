def func(args):
    print(args)


func(1)
func([1, 2, 3])
func({"x": 1, "y": 2})
func({1, 2, 3})


def func_two(*args):  # >-1
    print(*args)


func_two(1)
func_two([1, 2, 3])
func_two({"x": 1, "y": 2})
func_two({1, 2, 3})



