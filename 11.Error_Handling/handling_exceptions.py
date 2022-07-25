import random


def raise_exception():
    chance = 0.7
    if random.random() < chance:
        raise ValueError("Invalid value")


for _ in range(100):
    try:
        # Code MAY raise an exception
        raise_exception()
        print("No exception")

    except (ValueError, TypeError) as error:
        print("Value error handled!")
        print(error)

    finally:
        print("This is finally")
"""
Code block "Try" could raise an exception but could be correct also
The error should be predicted correctly
If exception occurs, the code below the raise is not executed

Except block is managing the specific exception raised in the "Try" block
In "Except" block is possible to catch multiple exceptions if different exceptions are handled the same way
If different exceptions will be handled differently, creation of multiple "Except" blocks is required

Finally block is ALWAYS executed
"""

