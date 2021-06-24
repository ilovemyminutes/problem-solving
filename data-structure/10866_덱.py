from collections import deque

n = int(input())
commands = [input().strip().split() for _ in range(n)]

que = deque([])

for command in commands:
    if len(command) == 2:
        command, value = command
        if command == 'push_front':
            que.appendleft(value)
        elif command == 'push_back':
            que.append(value)
    else:
        command = command[0]
        if command == 'front':
            if que:
                print(que[0])
            else:
                print(-1)
        elif command == 'back':
            if que:
                print(que[-1])
            else:
                print(-1)
        elif command == 'pop_front':
            if que:
                popped = que.popleft()
                print(popped)
            else:
                print(-1)
        elif command == 'pop_back':
            if que:
                popped = que.pop()
                print(popped)
            else:
                print(-1)
        elif command == 'size':
            print(len(que))
        elif command == 'empty':
            if que:
                print(0)
            else:
                print(1)
