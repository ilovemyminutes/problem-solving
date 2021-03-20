'''
c: 시선이 시작될 수 있는 지점
x: 비선호 콘텐츠
.: 선호 콘텐츠
'''
from collections import deque
n_col, n_row = list(map(int, input().split()))
graph = []
c_locs = []

for i in range(n_row):
    row = list(input())
    graph.append(row)
    if i == 0:
        for idx, k in enumerate(row):
            if k == 'c':
                c_locs.append(idx)

def get_movable_list(graph, loc, n_col, n_row) -> list:
    direction = {'left': [0, -1], 'right': [0, 1], 'down': [1, 0]}

    movable_list = []
    for k, v in direction.items():
        if (loc[0]+v[0] < n_row) and (loc[1]+v[1] < n_col) \
            and (loc[0]+v[0] >= 0) and (loc[1]+v[1] >= 0): # 이동 가능 여부
            post_loc = (loc[0]+v[0], loc[1]+v[1])
            if graph[post_loc[0]][post_loc[1]] == '.': # 선호 콘텐츠
                movable_list.append((k, post_loc))
    return movable_list

def search_path(graph, start, n_col, n_row):
    path = [[0]*n_col for _ in range(n_row)]
    path[0][start[-1]] = 1

    que = deque([start])
    while que:
        current = que.popleft()
        movable_list = get_movable_list(graph, current, n_col, n_row)
        for d, (x, y) in movable_list:
            path[x][y] = path[current[0]][current[1]] + 1
            que.append((x,y))
            if any(path[-1]): # 도착
                min_len = min(list(filter(lambda x: x > 0, path[-1])))
                return min_len, path

paths = []
for c in c_locs:
    start = (0, c)
    min_len, path = search_path(graph, start, n_col, n_row)
    paths.append((min_len, path))

optimized = min(paths, key=lambda x: x[0])
for p in optimized[-1]:
    print(p)