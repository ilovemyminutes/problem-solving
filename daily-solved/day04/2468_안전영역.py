'''https://www.acmicpc.net/problem/2468
문제:
    - 비가 내렸을 때 물에 잠기지 않는 안전한 영역 최대 수
    - 일정한 높이 이하의 모든 지점은 물에 잠긴다
    - 안전 영역: 물에 잠기지 않는 지점들이 상하좌우로 적어도 하나 인접 & 그 크기가 최대
입력:   
    - N: 2 이상 1백 이하
생각:
    - 물에 잠기는 지점 먼저 체크
'''
import sys
from copy import deepcopy
input = sys.stdin.readline

def apply_rain(graph, rain: int):
    # 잠길 경우 True, 그렇지 않을 경우 False
    graph = [list(map(lambda x: x <= rain, row)) for row in graph]
    return graph

def move_list(loc, n: int):
    dx_list, dy_list = [0, 0, 1, -1], [1, -1, 0, 0]
    output = []
    for dx, dy in zip(dx_list, dy_list):
        nxt_x, nxt_y = loc[0] + dx, loc[1] + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < n:
            output.append((nxt_x, nxt_y))
    return output

def dfs(loc, n):
    stack = [loc]
    while stack:
        cur_x, cur_y = stack.pop()
        visited[cur_y][cur_x] = True
        for nxt_x, nxt_y in move_list(loc=(cur_x, cur_y), n=n):
            if not tmp_graph[nxt_y][nxt_x] and not visited[nxt_y][nxt_x]:
                stack.append((nxt_x, nxt_y))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_num_regions = 0
for rain in range(0, 100+1):
    num_regions = 0
    tmp_graph = deepcopy(graph)
    tmp_graph = apply_rain(tmp_graph, rain=rain)
    
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not tmp_graph[y][x] and not visited[y][x]:
                dfs(loc=(x, y), n=n)
                num_regions += 1

    if max_num_regions < num_regions:
        max_num_regions = num_regions

print(max_num_regions)
