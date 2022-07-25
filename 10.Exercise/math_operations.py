from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)

    while numbers:
        number = numbers.popleft()
        kwargs["a"] += number

        if not numbers:
            break

        number = numbers.popleft()
        kwargs["s"] -= number

        if not numbers:
            break

        number = numbers.popleft()
        if number != 0:
            kwargs["d"] /= number

        if not numbers:
            break

        number = numbers.popleft()
        kwargs["m"] *= number

    sorted_result = [f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]

    return "\n".join(sorted_result)

