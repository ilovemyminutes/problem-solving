"""바이러스, https://www.acmicpc.net/problem/2606"""
n_nodes = int(input())
n_links = int(input())
graph = {i: [] for i in range(1, n_nodes + 1)}

for _ in range(n_links):  # 순서는 상관 없음
    node1, node2 = tuple(map(int, input().split()))
    if node2 not in graph[node1]:
        graph[node1].append(node2)
    if node1 not in graph[node2]:
        graph[node2].append(node1)

visited = [0 for _ in range(n_nodes)]


def dfs(graph, visited, start=1):
    network_size = 0
    stack = [start]
    while stack:
        origin = stack.pop()
        if visited[origin - 1] == 0:  # 미방문
            visited[origin - 1] = 1
            network_size += 1
        for adj in graph[origin]:
            if visited[adj - 1] == 0:
                stack.append(adj)
    return network_size - 1


print(dfs(graph, visited, 1))
