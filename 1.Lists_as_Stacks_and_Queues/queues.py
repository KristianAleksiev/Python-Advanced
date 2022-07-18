# Enqueue - push
# Dequeue - pop - popleft()
# Peek
# Count

# Very slow, list execution
q = []
q.append(1)
q.append(2)
q.append(3)
q.pop(0)

# Implemented, faster execution
from collections import deque
q = deque()
q.append(2)
q.appendleft(3)
q.pop()
q.popleft()


# Queueing
# [1]
# [1, 2]
# [1, 2, 3]

# Queueing
# [1, 2, 3]
# [2, 3]
# [3]

