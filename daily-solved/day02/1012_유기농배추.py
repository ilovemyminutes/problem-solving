'''https://www.acmicpc.net/problem/1012

입력: 테스트 케이스 개수 T
각 테스트에 대해 가로 길이 M, 새로 길이 N, 배추가 심어져 있는 위치의 개수 K. K개의 배추 좌표
출력: 필요한 최소의 지렁이 수

목적: 그룹 수 구하기

생각:
    - 루프 돌면서 양배추가 발견될 때 DFS로 완전탐색하면 되겠다
    - 방문처리는 어떤 방식이 좋으려나?
'''
from copy import deepcopy

def dfs(loc: tuple, num_cols: int, num_rows: int):
    dx_list = [0, 0, +1, -1] 
    dy_list = [+1, -1, 0, 0] # 상하우좌

    stack = [loc]
    while stack:
        x, y = stack.pop()
        visited[(x, y)] = True
        
        for dx, dy in zip(dx_list, dy_list):
            nxt_x, nxt_y = x + dx, y + dy
            if 0 <= nxt_x < num_cols and 0 <= nxt_y < num_rows and graph[nxt_y][nxt_x] == 1 and visited[(nxt_x, nxt_y)] is False:
                stack.append((nxt_x, nxt_y))


# initialize
t = int(input()) # 테스트 케이스 개수
test_cases = dict()

for t_idx in range(t):
    m, n, k = map(int, input().split()) # 열의 수, 행의 수, 배추 개수
    graph = [[0]*m for _ in range(n)]

    cabbages = []
    visited = dict()

    # 배추 좌표
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        cabbages.append((x, y))
        visited[(x, y)] = False # 미방문
    
    test_cases[t_idx] = dict(m=m, n=n, cabbages=deepcopy(cabbages), visited=deepcopy(visited), graph=deepcopy(graph))

# get num groups
for t_idx in range(t):
    test_case = test_cases[t_idx]
    m = test_case['m']
    n = test_case['n']
    cabbages = test_case['cabbages']
    visited = test_case['visited']
    graph = test_case['graph']

    num_groups = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and visited[(x, y)] is False:
                dfs((x, y), num_cols=m, num_rows=n)
                num_groups += 1
                
    print(num_groups)



    

    

        
        

        

        
        