'''https://www.acmicpc.net/problem/7569
문제:
    - shape (n, m, h)인 3차원 배열
    - 인접하다 :=  위, 아래, 왼쪽, 오른쪽, 앞, 뒤 6방향

입력:
    - M, N, H (열, 행, 높이)
        - M, N: 2 이상 100 이하
        - N: 1 이상 100 이하
    - 1: 익토, 0: 안익토, -1: 없음
'''
import sys
from collections import deque
input = sys.stdin.readline

def get_move_list(loc, m, n, h) -> list: # loc: (h, n, m)
    # 평면 내 상하좌우 + 위아래
    dx_list = [0, 0, +1, -1, 0, 0] # m 
    dy_list = [+1, -1, 0, 0, 0, 0] # n
    dz_list = [0, 0, 0, 0, +1, -1] # h
    z, y, x = loc

    move_list = []
    for dx, dy, dz in zip(dx_list, dy_list, dz_list):
        nxt_x = x + dx
        nxt_y = y + dy
        nxt_z = z + dz
        
        # 그래프 내 좌표 & 안익은 토마토
        if 0 <= nxt_x < m and 0 <= nxt_y < n and 0 <= nxt_z < h and graph[nxt_z][nxt_y][nxt_x] == 0:
            move_list.append((nxt_z, nxt_y, nxt_x))
    
    return move_list

# initialize
m, n, h = map(int, input().split()) # 가로, 세로, 높이
graph = [] # (H, N, M)
ripes = deque([]) # (H, N, M, DATE): 익은 토마토 좌표 + 익은 날짜
num_unripes = 0

for h_idx in range(h):
    square = []
    for n_idx in range(n):
        row = list(map(int, input().split())) # 길이 n
        square.append(row)
        subripes = []
        for m_idx, v in enumerate(row):
            if v == 1:
                ripes.append((h_idx, n_idx, m_idx, 0))
            elif v == 0:
                num_unripes += 1
    graph.append(square)

# solve 
total_dates = 0
while ripes:
    ripe = ripes.popleft()
    ripe_loc, date = ripe[:3], ripe[3]
    total_dates = date if date > total_dates else total_dates
    unripe_locs = get_move_list(ripe_loc, m, n, h)
    for loc in unripe_locs:
        graph[loc[0]][loc[1]][loc[2]] = 1
        num_unripes -= 1
        ripes.append((loc[0], loc[1], loc[2], date+1))

if num_unripes > 0:
    print(-1)
else:
    print(total_dates)



