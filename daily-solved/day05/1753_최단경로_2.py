'''https://www.acmicpc.net/problem/1753
각 정점은 1부터 V까지 넘버링
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e+9)

v, e = map(int, input().split())
k = int(input()) # 시작점 번호

# 각 노드가 어떤 노드와 연결되어 있는지
# 해당 연결에는 얼만큼의 weight가 부여됐는지
# NOTE. 서로 다른 두 정점 사이에는 여러 간선이 존재할 수 있음
graph = [[] for _ in range(v+1)]
weights = [INF] * (v+1)

for _ in range(e):
    n_out, n_in, w = map(int, input().split()) # u -> v, weight
    graph[n_out].append((w, n_in))

prior_q = []
heapq.heappush(prior_q, (0, k)) # 시작 노드 삽입
weights[k] = 0

while prior_q:
    cur_w, cur_loc = heapq.heappop(prior_q)
    if weights[cur_loc] < cur_w:
        continue
    
    for w, loc in graph[cur_loc]:
        cumul_w = cur_w + w
        if cumul_w < weights[loc]:
            weights[loc] = cumul_w
            heapq.heappush(prior_q, (cumul_w, loc))

for node_id in range(1, v+1):
    w = weights[node_id]
    if w == INF:
        print('INF')
    else:
        print(w)