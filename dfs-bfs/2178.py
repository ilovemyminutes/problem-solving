'''
1: 이동할 수 있는 칸
0: 이동할 수 없는 칸
'''
import sys

def move(loc, max_x, max_y):
    moved_loc_list = []
    dx_list = [0, 0, 1, 1]
    dy_list = [0, 1, 0, 1]
    for dx, dy in zip(dx_list, dy_list):
        if (loc[0] - dx < 0) or (loc[0] - dx >= max_x) or (loc[1] - dy < 0) or (loc[1] - dy >= max_y):
            continue
        moved_loc = (loc[0] - dx, loc[1] - dy)
        moved_loc_list.append(moved_loc)
    return moved_loc_list

n, m = map(int, input().split())
START = (0, 0)
ARRIVAL = (n-1, m-1)
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

visited = []
num_paths = 0
def dfs(graph: list, loc: tuple, arrival: tuple=ARRIVAL) -> int:
    global n
    global m
    global num_paths

    if loc == arrival:
        return num_paths

    for x, y in move(loc, n, m):
        if ((x, y) not in visited) and (graph[x][y] == 1):
            visited.append((x, y))
            loc = (x, y) # 이동
            dfs(graph, loc, arrival)
            print(loc)
            print(num_paths)
            print(visited)
        else:
            print('all visit')

    return num_paths

print(dfs(graph, loc=START, arrival=ARRIVAL))