'''https://www.acmicpc.net/problem/1504
문제:
    - 방향성 없는 그래프 
        - 노드 2 이상 8백 이하
        - 링크 0 이상 20만 이하
    - 임의로 주어진 두 정점은 반드시 통과
    - 한번 이동했던 정점/간선 다시 이동 가능
    - 반드시 최단 경로로 이동
'''
import sys
import heapq
INF = int(1e+9)
n, e = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(e):
    n1, n2, w = map(int, input().split())
    graph[n1].append((w, n2))
    graph[n2].append((w, n1))

m1, m2 = map(int, input().split())

case1 = 0 # 1 -> m1 -> m2 -> N
case2 = 0 # 1 -> m2 -> m1 -> N

for idx, start in enumerate([(0, 1), (0, m1), (0, m2)]):
    distances = [INF] * (n+1)
    prior_q = []
    heapq.heappush(prior_q, start)
    distances[start[1]] = 0

    while prior_q:
        cur_dist, cur_loc = heapq.heappop(prior_q)
        if distances[cur_loc] < cur_dist:
            continue
        
        for dist, loc in graph[cur_loc]:
            cumul_dist = cur_dist + dist
            if cumul_dist < distances[loc]:
                distances[loc] = cumul_dist
                heapq.heappush(prior_q, (cumul_dist, loc))
    if idx == 0:
        if case1 < INF:
            case1 += distances[m1]
        if case2 < INF:
            case2 += distances[m2]

    elif idx == 1:
        if case1 < INF:
            case1 += distances[m2]
        if case2 < INF:
            case2 += distances[n]

    elif idx == 2:
        if case1 < INF:
            case1 += distances[n]
        if case2 < INF:
            case2 += distances[m1]


shortest = min(case1, case2)
if shortest < INF:
    print(shortest)
else:
    print(-1)




