"""DFS와 BFS, https://www.acmicpc.net/problem/1260"""
from collections import deque

n, m, v = map(int, input().split())
graph = {i: [] for i in range(n)}
for _ in range(m):
    node_a, node_b = map(int, input().split())
    if node_a - 1 not in graph[node_b - 1]:
        graph[node_b - 1].append(node_a - 1)
    if node_b - 1 not in graph[node_a - 1]:
        graph[node_a - 1].append(node_b - 1)


def dfs(graph: dict, v: int) -> str:
    _sort_graph(graph, True)
    visited = list()
    v -= 1
    stack = [v]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        else:
            visited.append(node)
            for adj in graph[node]:
                if adj not in visited:  # 방문 안하고 인접한 것에 대해
                    stack.append(adj)
    answer = " ".join(list(map(lambda x: str(x + 1), visited)))
    return answer


def bfs(graph: dict, v: int) -> str:
    _sort_graph(graph, False)
    visited = list()
    v -= 1
    que = deque([v])
    while que:
        node = que.popleft()
        if node in visited:
            continue
        else:
            visited.append(node)
            for adj in graph[node]:
                if adj not in visited:
                    que.append(adj)
    answer = " ".join(list(map(lambda x: str(x + 1), visited)))
    return answer


def _sort_graph(graph, reverse=True):
    for k in graph.keys():
        graph[k] = sorted(graph[k], reverse=reverse)


print(dfs(graph, v))
print(bfs(graph, v))
