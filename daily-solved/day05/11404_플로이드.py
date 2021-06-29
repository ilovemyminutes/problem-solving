'''https://www.acmicpc.net/problem/11404
문제:
    - N개 도시(2 이상 1백 이하), M개 버스(1 이상 10만 이하)
'''
import sys
input = sys.stdin.readline
INF = int(1e+9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):
    graph[x][x] = 0 # diagonal

for _ in range(m):
    n1, n2, weight = map(int, input().split())

    # 간선이 여러개일 수 있음
    if weight < graph[n1][n2]:
        graph[n1][n2] = weight

for k in range(1, n+1): # 들렀다 갈 곳
    for start in range(1, n+1): # 출발지점 각각에 대해
        for arrival in range(1, n+1): # 각각의 도착점으로 도달하기 위한 최소비용
            graph[start][arrival] = min((graph[start][arrival], graph[start][k]+graph[k][arrival]))
                # NOTE. 연결되지 않은 경우 INF가 유지됨

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] >= INF:
            graph[a][b] = 0

for row in range(1, n+1):
    tmp = list(map(str, graph[row][1:]))
    print(' '.join(tmp))
