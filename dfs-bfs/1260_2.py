"""DFS와 BFS, https://www.acmicpc.net/problem/1260"""
import sys
from collections import deque


def _sort_graph(graph: dict, reverse: bool) -> dict:
    for key in graph.keys():
        graph[key].sort(reverse=reverse)
    return graph


def print_dfs(graph: dict, start: int) -> None:
    graph = _sort_graph(graph, reverse=True)

    dfs = []
    stack = [start]
    visited = []
    while stack:
        origin = stack.pop()
        if origin in visited:
            continue
        visited.append(origin)  # 방문 처리
        dfs.append(str(origin))  # 경로 추가
        for adj in graph[origin]:  # 미방문 노드 추가
            if adj not in visited:
                stack.append(adj)
    sys.stdout.write(" ".join(dfs))


def print_bfs(graph: dict, start: int) -> None:
    graph = _sort_graph(graph, reverse=False)

    bfs = []
    que = deque([start])
    visited = []

    while que:
        origin = que.popleft()
        if origin in visited:
            continue

        visited.append(origin)
        bfs.append(str(origin))  # 경로 추가
        for adj in graph[origin]:  # 미방문 노드 추가
            if adj not in visited:
                que.append(adj)
    sys.stdout.write(" ".join(bfs))


n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 not in graph[n2]:
        graph[n2].append(n1)
    if n2 not in graph[n1]:
        graph[n1].append(n2)

print_dfs(graph, start=v)
print()
print_bfs(graph, start=v)
