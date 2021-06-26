'''https://www.acmicpc.net/problem/18258

문제:
    push X: 정수 X를 큐에 넣는 연산이다.
    pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 큐에 들어있는 정수의 개수를 출력한다.
    empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
operations = [input().split() for _ in range(n)]

que = deque([])
for oper in operations:
    if len(oper) == 1:
        command = oper[0]
        if command == 'pop':
            print_output = que.popleft() if que else -1
        elif command == 'size':
            print_output = len(que)
        elif command == 'empty':
            print_output = 0 if que else 1
        elif command == 'front':
            print_output = que[0] if que else -1
        elif command == 'back':
            print_output = que[-1] if que else -1
        print(f'{print_output}\n')

    # push
    else:
        value = oper[1]
        que.append(value)
