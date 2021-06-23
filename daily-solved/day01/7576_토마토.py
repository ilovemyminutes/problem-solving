'''https://www.acmicpc.net/problem/7576
보관 후 하루가 지나면 익은 토마토와 '인접'한 익지 않은 토마토가 익게 됨
인접 := 특정 토마토로부터 좌우상하에 중 한 곳에 토마토가 위치할 경우
창고에 보관된 토마토가 언제 다 익는지 '최소 일수'를 구하라

입력:
    - 상자의 크기 2 <= N, M <= 1000
    - 그래프: 1(익토), 0(안익토), -1(노토)

출력:
    (자명)저장때부터 모든 토마토가 익어있을 경우: 0
    (불능)모두 익을 수 없을 경우: -1
    그 외: 모두 익기까지 걸리는 최소 날짜

생각들:
완전탐색까지 걸리는 시간으로 볼 수 있지 않을까? -> BFS!
- 아 근데 출발 지점에 1개보다 많을 수 있으니까 다시 생각해보자
- 여러 지점으로부터 BFS를 돌릴 수 있을 것 같은데
    - 초기 익토 지점만 골라서 전염되도록 함과 동시에 방문처리를 하면
      구현 상으로는 동시에 전염된 것이 아니지만, 결과적으로 동시에 전염된 상황을 재연할 수 있음
    - '현존하는' 익은 토마토에 대해서만 루프를 돌게하고 해당 루프를 다 돌았을 때 일자를 추가해주면 되겠다

하루마다 그래프가 갱신되는 걸 생각해봐야할까?
    - 불능: -1로 둘러쌓인 안익토(0)가 적어도 하나 있다 => 불능
        - 더 쉬운 방법: 익게할 토마토가 더이상 없는데 덜익은 토마토가 남았을 때
    - 자명: 0이 없다
    - 그 외: 
'''
from collections import deque
from copy import deepcopy

def move_list(loc, num_rows: int, num_cols: int) -> list:
    """이동 가능한(전염 가능한) 좌표 := 그래프에서 벗어나지 않음 & 방문한 적이 없음 & 익지 않음"""
    drows, dcols = [+1, -1, 0, 0], [0, 0, +1, -1]

    move_list = []
    for dr, dc in zip(drows, dcols):
        nxt_r, nxt_c = loc[0] + dr, loc[1] + dc
        if (0 <= nxt_r < num_rows) and (0 <= nxt_c < num_cols) and (graph[nxt_r][nxt_c] == 0):
            move_list.append((nxt_r, nxt_c))

    return move_list

# initialize
m, n = map(int, input().split()) # m(열개수), n(행개수)
graph = []
ripes = deque([])

for row_idx in range(n):
    row = list(map(int, input().split()))
    for col_idx, value in enumerate(row):
        if value == 1: # RIPE
            ripes.append((row_idx, col_idx)) # 익은 토마토 스택
    graph.append(row) # 그래프 구성

def bfs(ripes: deque, n, m):
    num_days = -1
    while ripes:
        for _ in range(len(ripes)):
            loc = ripes.popleft()
            for (r, c) in move_list(loc, num_cols=m, num_rows=n):
                graph[r][c] = 1
                ripes.append((r, c))
        num_days += 1
    
    for row in graph:
        if 0 in row:
            return -1

    return num_days

print(bfs(ripes, n, m))
