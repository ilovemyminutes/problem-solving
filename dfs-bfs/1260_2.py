import sys
from collections import defaultdict
n, m, v = map(int, input().split())

graph = []
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph.append((v1, v2))

graph.sort(key=lambda x: x[-1])
graph.sort(key=lambda x: x[0])

adj_dict = {i: [] for i in range(1, n+1)}
for v1, v2 in graph:
    adj_dict[v1].append(v2)

print(adj_dict)

def dfs(start, adj_dict):
    stack = [start]

    while True:
        node = stack.pop()
        adj_dict[node]