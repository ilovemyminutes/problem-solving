'''https://www.acmicpc.net/problem/1927'''
import heapq
import sys
input = sys.stdin.readline # 안하니까 시간초과
n = int(input())
values = [int(input()) for _ in range(n)]
heap = []

for v in values:
    if v == 0 and len(heap) == 0:
        print(0)
    elif v == 0 and len(heap) > 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, v)
