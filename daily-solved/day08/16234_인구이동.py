'''https://www.acmicpc.net/problem/16234
문제:
    - NxN 크기의 땅(1 이상 50 이하)
    - A[r][c]: 거주민 수
    - 다음과 같은 인구 이동이 더이상 발생할 수 없을 때까지 반복
        - 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라 간 국경선 하루동안 개방
            - 각 국가의 초기 인구는 0명 이상 1백명 이하
        - 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
        - '연합': 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있을 경우
        - 연합을 이루고 있는 각 칸의 인구수: (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
            - 즉, 연합을 맺은 국가들의 인구수 평균
            - 소수점은 버림
        - 연합을 해체하고, 모든 국경선을 닫는다.
    - 인구이동은 2천회 이하로 발생하도록 그래프가 주어짐
    - BFS/DFS로 완전탐색으로 '연합' 분포를 찾은 뒤, 국경문을 열어 인구수 갱신
        - 더이상 연합 분포가 존재하지 않을 경우 종료

'''
import sys
import math
input = sys.stdin.readline

def move_list(loc: tuple) -> list:
    dx_list, dy_list = [0, 0, -1, 1], [-1, 1, 0, 0]
    output = []
    for dx, dy in zip(dx_list, dy_list):
        nxt_x, nxt_y = loc[0] + dx, loc[1]  + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < n:
            output.append((nxt_x, nxt_y))
    return output

def get_coalition(loc: tuple, l: int, r: int) -> dict:
    members = []
    population = []
    stack = [loc]
    while stack: # dfs
        cur_x, cur_y = stack.pop()
        visited[cur_y][cur_x] = True
        members.append((cur_x, cur_y))
        population.append(graph[cur_y][cur_x])

        for x, y in move_list(loc=(cur_x, cur_y)):
            if not visited[y][x] and l <= abs(graph[cur_y][cur_x]-graph[y][x]) <= r:
                stack.append((x, y))
    coalition = dict( 
        members=members, # [(국가1 좌표), (국가2 좌표), ...]
        population=math.floor(sum(population)/len(population)) # 평균 인구
        ) if len(members) > 1 else None # 연합이 자기 자신뿐일 경우 None
    return coalition

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

num_movements = 0
while True:
    visited = [[False]*n for _ in range(n)]
    coalitions = []
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue
            coalition = get_coalition(loc=(x, y), l=l, r=r)
            coalitions.append(coalition)

    # 연합군이 하나도 없을 경우 인구이동 종료
    if not any(coalitions):
        break
    
    for coal in coalitions:
        members = coal['members']
        population = coal['population']
        for (x, y) in members:
            graph[y][x] = population
    num_movements += 1

print(num_movements)

            





