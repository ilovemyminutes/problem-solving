"""
AC: 정수 배열 연산을 위한 언어
- R(뒤집기): 배열의 순서를 뒤집음
- D(버리기): 첫번째 수를 버림
  - 배열이 비어있을 경우 에러 raise
- 함수는 조합하여 사용할 수 있음 (RDD <=> 'R -> D -> D')
"""
import sys
from collections import deque
input = sys.stdin.readline
output = ''

t = int(input())  # 1~100
for _ in range(t):
    p = input().strip()  # 1 <= len(p) <= 100K
    _ = input()

    # init array
    arr = input().strip()[1:-1]
    if len(arr) == 0:
        arr = deque([])
    else:
        arr = deque(arr.split(','))

    # apply operations
    is_error = False
    num_reverse = 0
    for op in p:
        if op == 'R':
            num_reverse += 1
        elif op == 'D':
            if len(arr) == 0:
                is_error = True
                break
            elif num_reverse % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    
    # save output
    if is_error:
        output += 'error\n'
    else:
        if num_reverse % 2 == 1:
            arr.reverse()
        output += f"[{','.join(arr)}]\n"

print(output.strip())