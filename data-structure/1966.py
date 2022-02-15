"""
queue 내 k번째 원소가 몇 번째로 인쇄될지 맞추기
- queue 내 가장 앞 원소의 중요도 확인
- 나머지 원소 중 중요도 높은 원소가 하나라도 있으면 queue 가장 뒤에 재배치
  - 그렇지 않을 경우 출력
"""
import sys
from collections import deque
input = sys.stdin.readline

output = []

t = int(input())
for _ in range(t):
    _, target_idx = map(int, input().split())
    imps = [(imp, idx) for idx, imp in enumerate(map(int, input().split()))]  # importances

    queue = deque(imps)
    order = 0
    while len(queue) > 0:
        cur_imp, cur_idx = queue.popleft()

        revolve = False
        for imp, idx in queue:
            if cur_imp < imp:
                revolve = True
                break

        if revolve:
            queue.append((cur_imp, cur_idx))
        else:
            order += 1
            if cur_idx == target_idx:
                break
    output.append(order)

for o in output:
    print(o)

