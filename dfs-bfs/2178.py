"""https://www.acmicpc.net/problem/2178
1: 이동할 수 있는 칸
0: 이동할 수 없는 칸
"""
import sys
from collections import deque


def move(loc, n: int, m: int):
    movable_list = []
    dx_list, dy_list = [0, 0, -1, 1], [-1, 1, 0, 0]
    for dx, dy in zip(dx_list, dy_list):
        if (
            (loc[0] + dx < 0)
            or (loc[0] + dx >= n)
            or (loc[1] + dy < 0)
            or (loc[1] + dy >= m)
        ):
            continue
        moved_loc = (loc[0] + dx, loc[1] + dy)
        movable_list.append(moved_loc)
    return movable_list


def get_shortest_path_len(graph: list, n, m) -> int:
    """BFS를 활용해 최단 경로를 리턴
    [input]
    101111
    101010
    101011
    111011

    get shortest length
    [1, 0, 0, 0, 0, 0]
    [2, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0]
    ...
    [1, 0, 9, 10, 11, 12]
    [2, 0, 8, 0, 12, 0]
    [3, 0, 7, 0, 13, 14]
    [4, 5, 6, 0, 14, 15] <- 최단 경로: 15
    """
    start = (0, 0)
    path = [[0] * m for _ in range(n)]

    que = deque([start])
    path[start[0]][start[0]] = 1  # depth = 1

    while que:
        current = que.popleft()
        for x, y in move(current, n, m):
            if path[x][y] == 0 and graph[x][y] == 1:
                path[x][y] = path[current[0]][current[1]] + 1
                que.append((x, y))

        # To check path graph
        # for row in path:
        #     print(row)
        # print()

    return path[-1][-1]


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

print(get_shortest_path_len(graph, n, m))
