"""https://www.acmicpc.net/problem/7576
익지 않은 토마토는 익은 토마토의 영향을 받음
0: 익지 않은 토마토
1: 익은 토마토
-1: 토마토가 들어있지 않은 칸
- 토마토는 1개 이상 주어짐

출력
- 토마토가 모두 익기까지 걸리는 일수를 출력
- 모두 익는 것이 불가능할 경우 -1을 출력

최단 경로 문제랑 똑같은것같은데?
"""
import sys

m, n = map(int, input().split()) # n: 가로 수, m: 세로 수
graph = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

affected = []

def get_raw_adj(graph: list, loc: list, n: int, m: int) -> list:
    '''인접한 익지 않은 토마토 위치를 리턴'''
    dx_list, dy_list = [0, 0, -1, 1], [-1, 1, 0, 0]

    output = []
    for dx, dy in zip(dx_list, dy_list):
        if (loc[0] + dx < 0) or (loc[0] + dx >= n) or (loc[1] + dy < 0) or (loc[1] + dy >= m): # is in?
            post_loc = (loc[0] + dx, loc[1] + dy)
            if graph[post_loc[0]][post_loc[1]] == 0: # is raw?
                output.append(post_loc)
    return output


