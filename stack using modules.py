import collections
stack=collections.deque()
print(stack)
stack.append(10)
stack.append(80)
stack.append(40)
stack.append(30)
stack.append(20)
print(stack)


import queue
stack=queue.LifoQueue(3)                #maximim size is 3
stack.put(10)
stack.put(90)
stack.put(80)
#stack.put(22,timeout=1)
print(stack)
stack.get()
stack.get()
stack.get()
stack.get(timeout=1)
print(stack)