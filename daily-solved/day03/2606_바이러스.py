'''https://www.acmicpc.net/problem/2606
문제:
    - 1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터 수
생각:
    - 1번 노드에서 완전탐색하면 되겠네
    - 1번 컴퓨터 
'''
from copy import deepcopy

# initialize
n = int(input()) # 컴퓨터 대수
num_links =  int(input()) # 링크 수
graph = {i:[] for i in range(1, n+1)}
visited = [False for _ in range(n+1)]

for _ in range(num_links):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

infected = []
stack = deepcopy(graph[1])
visited[1] = True

# dfs
while stack:
    current = stack.pop()
    infected.append(current)
    visited[current] = True

    candidates = graph[current]
    for c in candidates:
        if visited[c] is not True:
            stack.append(c)

print(len(set(infected)))

