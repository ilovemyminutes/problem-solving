'''https://www.acmicpc.net/problem/1753
문제:
    - 방향그래프가 주어졌을 때, 시작점에서 나머지 정점으로의 최단 거리를 구하시오
    - 모든 간선 가중치 <= 10

입력:
    - V, E: 정점(1 이상 2만 이하), 간선(1 이상 30만 이하)
        - 정점은 1부터 V까지 숫자 부여
    - K: 시작 정점의 번호

출력:
    - 시작점 자신: 0
    - 경로가 없는 경우: INF
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e+9)

# initialize
v, e = map(int, input().split())
k = int(input()) # start node
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    n1, n2, w = map(int, input().split())
    graph[n1].append((w, n2)) # (WEIGHT, VERTEX ID)

# solve
priority_que = []
heapq.heappush(priority_que, (0, k)) # (WEIGHT, VERTEX ID)
distance[k] = 0

while priority_que:
    cur_dist, cur_loc = heapq.heappop(priority_que)
    if distance[cur_loc] < cur_dist:
        continue

    # 현 노드와 연결된 노드
    for dist, loc in graph[cur_loc]: 
        cost = cur_dist + dist # 기준 노드에서 해당 노드까지의 비용
        if cost < distance[loc]: # 작으면 최소 비용 갱신
            distance[loc] = cost
            heapq.heappush(priority_que, (cost, loc))

for node_id in range(1, v+1):
    dist = distance[node_id]
    if dist == INF:
        print('INF')
    else:
        print(dist)
        