"""유기농 배추, https://www.acmicpc.net/problem/1012"""


def _get_zero_matrix(shape: tuple) -> list:
    m, n = shape  # 가로 길이, 세로 길이
    return [[0 for _ in range(m)] for _ in range(n)]


def _get_adj(m: int, n: int, x, y):
    if x == 0 and y == 0:
        return (x + 1, y), (x, y + 1)
    elif x == m - 1 and y == n - 1:
        return (x - 1, y), (x, y - 1)
    elif x == 0:
        return (x, y - 1), (x + 1, y), (x, y + 1)
    elif x == m - 1:
        return (x, y - 1), (x - 1, y), (x, y + 1)
    elif y == 0:
        return (x - 1, y), (x + 1, y), (x, y + 1)
    elif y == n - 1:
        return (x - 1, y), (x + 1, y), (x, y - 1)
    else:
        return (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)


n_tests = int(input())
m_list, n_list, k_list = [], [], []
graph_list, visited_list = [], []

for _ in range(n_tests):
    m, n, k = map(int, input().split())  # 가로 길이, 세로 길이, 배추 위치 수
    graph = _get_zero_matrix((m, n))
    visited = dict()
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        visited[(x, y)] = 0
    graph_list.append(graph)
    visited_list.append(visited)
    m_list.append(m)
    n_list.append(n)


def dfs(graph, visited, shape: tuple, origin: tuple):
    stack = [origin]
    while stack:
        x, y = stack.pop()
        visited[(x, y)] = 1
        for adj in _get_adj(shape[0], shape[1], x, y):
            if adj in visited.keys() and visited[adj] == 0:
                stack.append(adj)


for t in range(n_tests):
    graph = graph_list[t]
    visited = visited_list[t]
    m = m_list[t]
    n = n_list[t]
    answer = 0
    while not all(visited.values()):
        for y, row in enumerate(graph):
            for x, value in enumerate(row):
                if (x, y) in visited.keys() and visited[(x, y)] == 0:
                    dfs(graph, visited, (m, n), (x, y))
                    answer += 1
    print(answer)
