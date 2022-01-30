import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
commands = [input().strip() for _ in range(n)]

queue = deque()
for c in commands:
    if c.startswith('push'):
        v = int(c.split()[-1])
        queue.append(v)
    elif c == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif c == 'size':
        print(len(queue))
    elif c == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)