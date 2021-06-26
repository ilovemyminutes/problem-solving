'''https://www.acmicpc.net/problem/11279
문제:
    - 배열에 자연수 x를 넣는다.
    - 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
        - 0이 입력될 경우 pop
'''
import sys
import heapq
input = sys.stdin.readline

# initialize
n = int(input())
operations = [int(input()) for _ in range(n)]

# solve
heap = []
for oper in operations:
    if oper == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-oper, oper))