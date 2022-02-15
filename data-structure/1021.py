"""양방향 순환큐
인덱싱을 1부터 시작 (편의상 구현 시 1씩 빼줌)
"""
from collections import deque

def op2(arr: deque):
    tmp = arr.popleft()
    arr.append(tmp)
    return arr

def op3(arr: deque):
    tmp = arr.pop()
    arr.appendleft(tmp)
    return arr

n, _ = map(int, input().split())
targets = [int(i)-1 for i in input().split()]
num_ops = 0

arr = deque([i for i in range(n)])
for t in targets:

    for i, a in enumerate(arr):
        if a == t:
            loc = i
            break

    left, right = loc, len(arr) - loc
    if left < right:
        for _ in range(left):
            op2(arr)
        num_ops += left
    else:
        for _ in range(right):
            op3(arr)
        num_ops += right

    arr.popleft()
            
print(num_ops)