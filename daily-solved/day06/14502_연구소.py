'''https://www.acmicpc.net/problem/14502
문제:
    - 연구소 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값
    - 연구소 크기: NxM
    - 새로 세울 수 있는 벽의 수: 3
    - 0 빈칸, 1 벽, 2 바이러스

해결:
    - 3 <= N, M <= 8 이라서 3중 for문 돌려도 될 것 같다
'''
import sys
from copy import deepcopy
from itertools import combinations
from tqdm import tqdm
input = sys.stdin.readline

def move_list(loc):
    dx_list, dy_list = [0, 0, -1, 1], [1, -1, 0, 0]
    output = []
    for dx, dy in zip(dx_list, dy_list):
        nxt_x, nxt_y = loc[0] + dx, loc[1] + dy
        if 0 <= nxt_x < m and 0 <= nxt_y < n:
            output.append((nxt_x, nxt_y))
    return output

def dfs(loc):
    stack = [loc] # 바이러스 위치
    while stack:
        cur_x, cur_y = stack.pop()
        visited[cur_y][cur_x] = True
        for x, y in move_list((cur_x, cur_y)):
            if current_graph[y][x] == 0:
                current_graph[y][x] = 2
                current_empty_locs.remove((x, y))
                stack.append((x, y))

n, m = map(int, input().split()) # (세로길이, 가로길이)
graph = []
empty_locs = []
virus_locs = []

for y in range(n):
    row = list(map(int, input().split()))
    for x, value in enumerate(row):
        if value == 0:
            empty_locs.append((x, y))
        elif value == 2:
            virus_locs.append((x, y))
    graph.append(row)

num_safes = 0
for e1, e2, e3 in combinations(empty_locs, r=3):
    current_graph = deepcopy(graph)
    current_empty_locs = deepcopy(empty_locs)
    visited = [[False] * m for _ in range(n)]

    for x, y in [e1, e2, e3]:
        current_graph[y][x] = 1
        current_empty_locs.remove((x, y))
    
    for x, y in virus_locs:
        if not visited[y][x]:
            dfs((x, y))

    if len(current_empty_locs) > num_safes:
        num_safes = len(current_empty_locs)
            
print(num_safes)
            
            