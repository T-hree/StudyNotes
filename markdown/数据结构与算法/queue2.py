# -- coding: utf-8 --
from collections import deque

q = deque(iterable=[1, 2, 3], maxlen=5)  # iterable初始队列元素 maxlen 最大长度 队满自动错位
q.append(4)  # 队尾进队
q.append(5)  # 队尾进队
q.append(6)  # 队尾进队
print(q)
print(q.popleft())  # 队首出队
print(q)

# 用于双向队列
q.appendleft(1)  # 队首进队
print(q.pop())  # 队尾出队


# 用队列 实现 tail 功能
def tail(n):
    with open("queue2.py", 'r') as f:
        q = deque(f, n)
        return q


print(tail(5))
