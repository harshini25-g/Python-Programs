import collections
q=collections.deque()
print(q)
q.appendleft(10)               #or use append and popleft
q.appendleft(90)
q.appendleft(50)
print(q)
print(q[-1])
print(q[-0])