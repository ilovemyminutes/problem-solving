"""
- N개 수에 대한 오름차순 정렬 (1~10M)
- 메모리 초과 이슈: 카운팅을 해야겠는데
- 우선순위큐로 안해도 됐겠다
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
pqueue = []  # 우선순위큐
counter = dict()

for _ in range(n):
    num = int(input())
    if num not in counter:
        counter[num] = 1
        heapq.heappush(pqueue, num)  # O(logn)
    else:
        counter[num] += 1

for _ in range(len(pqueue)):
    num_asc = heapq.heappop(pqueue)  # O(logn)
    for _ in range(counter[num_asc]):
        print(num_asc)
