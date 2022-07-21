import sys
from io import StringIO

test_input1 = """3, 6
1 2 3 4 5
6 7 8 9 10
11 12 13 14
"""

test_input2 = """1 2 3
4 5 6
7 8 9
"""
sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

print(input())
print(input())
