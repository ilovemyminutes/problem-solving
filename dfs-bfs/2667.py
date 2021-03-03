"""단지번호붙이기, https://www.acmicpc.net/problem/2667"""
n = int(input())  # 지도 크기
graph = list()
for _ in range(n):
    graph.append(list(map(int, list(input()))))


def solution(graph, n):
    visited = _get_visited(graph, n)
    x, y = 0, 0
    apartments = list()
    while not all(visited.values()):
        if graph[y][x] == 0 or visited[(x, y)] == 1:
            if x <= n - 2:
                x += 1
            else:
                x = 0
                y += 1
            continue
        else:
            if visited[(x, y)] == 0:
                apartments.append(dfs(graph, visited, (x, y)))
    raw_answer = sorted(list(map(lambda x: len(x), apartments)))

    print(len(raw_answer))
    for i in raw_answer:
        print(i)


def dfs(graph, visited, start: tuple):
    stack = [start]
    result = list()
    while stack:
        x0, y0 = stack.pop()
        result.append((x0, y0))
        visited[(x0, y0)] = 1
        for adj in _get_adj(n, x0, y0):
            x1, y1 = adj[0], adj[1]
            if (x1, y1) in visited.keys():
                if visited[(x1, y1)] == 0 and graph[y1][x1] == 1:
                    stack.append(adj)
    return set(result)


def _get_visited(graph, n):
    visited = dict()
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 1:
                visited[(x, y)] = 0
    return visited


def _get_adj(n: int, x: int, y: int):
    if x == 0 and y == 0:
        return (x + 1, y), (x, y + 1)
    elif x == n - 1 and y == n - 1:
        return (x - 1, y), (x, y - 1)
    elif x == 0:
        return (x, y - 1), (x + 1, y), (x, y + 1)
    elif x == n - 1:
        return (x, y - 1), (x - 1, y), (x, y + 1)
    elif y == 0:
        return (x - 1, y), (x + 1, y), (x, y + 1)
    elif y == n - 1:
        return (x - 1, y), (x + 1, y), (x, y - 1)
    else:
        return (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)
