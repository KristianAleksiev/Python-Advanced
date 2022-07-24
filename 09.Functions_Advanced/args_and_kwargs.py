def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3)
func(a=1, b=2, c=3)
func(1, 2, 3, a=4)


def func2(x, *args, **kwargs):
    print(f"x= {x}, args={args}, kwargs={kwargs}")


func2(1)
func2(1, 2)
func2(1, 2, b=7)
func2(1, 5, 7, 8, a=9)
func2(x=11)  # N.B.!!!
func2(x=11, y=15)

"""Function working abstractly despite the arguments"""
