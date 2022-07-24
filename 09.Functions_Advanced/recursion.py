def loop(n):
    if n < 0:
        return

    print(n)
    loop(n - 1)
    print(n)


loop(5)
