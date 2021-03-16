'''
1: 이동할 수 있는 칸
0: 이동할 수 없는 칸
'''
import sys
from collections import deque

def move(loc, n: int, m: int):
    '''loc: (x, y)
    Up: (x, y-1)
    Down: (x, y+1)
    Left: (x-1, y)
    Right: (x+1, y)
    '''
    move_list = []
    dx_list = [0, 0, -1, 1]
    dy_list = [-1, 1, 0, 0]
    for dx, dy in zip(dx_list, dy_list):
        if (loc[0] + dx < 0) or (loc[0] + dx >= n) or (loc[1] + dy < 0) or (loc[1] + dy >= m):
            continue
        moved_loc = (loc[0] + dx, loc[1] + dy)
        move_list.append(moved_loc)
    return move_list


def bfs(graph: list, n, m, loc: tuple, arrival: tuple) -> int:
    global num_paths

    if loc == arrival:
        return num_paths

    move_list = deque([])
    for x, y in move(loc, n, m):
        if ((x, y) not in visited) and (graph[x][y] == 1): # 방문한 곳이 아니고 벽이 아닌 경우
            move_list.append((x, y))
            # visited.append((x, y)) # 방문 처리
            # loc = (x, y) # 이동
            # num_paths += 1
    
    bfs(graph, n, m, loc, arrival)
    return num_paths


# def dfs(graph: list, n, m, loc: tuple, arrival: tuple) -> int:
#     global num_paths

#     if loc == arrival:
#         return num_paths

#     for x, y in move(loc, n, m):
#         if ((x, y) not in visited) and (graph[x][y] == 1): # 방문한 곳이 아니고 벽이 아닌 경우
#             visited.append((x, y)) # 방문 처리
#             loc = (x, y) # 이동
#             num_paths += 1
#             dfs(graph, n, m, loc, arrival)
#     return num_paths

n, m = map(int, input().split())
START = (0, 0)
ARRIVAL = (n-1, m-1)
num_paths = 0

graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

visited = [START]

print(dfs(graph, n, m, START, ARRIVAL))