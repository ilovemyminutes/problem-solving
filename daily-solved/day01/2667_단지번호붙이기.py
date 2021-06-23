"""https://www.acmicpc.net/problem/2667
지도를 입력해 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬해 출력
연결 := 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우(대각선은 연결이 아님)

입력: 단지 그래프
출력: 단지별 주택 수를 오름차순으로 출력
"""
IS_HOME = 1

def get_move_list(loc: tuple, num_rows: int, num_cols: int) -> list:
    """이동할 위치 리스트를 리턴.
    이동 가능 위치 := 인덱스가 그래프를 초과하거나 음수가 아니며 주택인 경우
    """
    move_list = []
    cur_r, cur_c = loc
    drows, dcols = [0, 0, +1, -1], [+1, -1, 0, 0]
    for drow, dcol in zip(drows, dcols):
        r = cur_r + drow
        c = cur_c + dcol
        if r < num_rows and r >= 0 and c < num_cols and c >= 0 and graph[r][c] == 1:
            move_list.append((r, c))
    return move_list

def update_visited(loc: tuple) -> None:
    r, c = loc
    visited[r][c] = True

# NOTE: stack이 없어도 되는거 같은데?
# def dfs(loc: tuple, group) -> None:
#     stack = [loc]
#     while stack:
#         cur_loc = stack.pop()
#         update_visited(cur_loc)
#         group.append(cur_loc)

#         move_list = get_move_list(cur_loc)
#         for nxt_loc in move_list:
#             r, c = nxt_loc
#             if visited[r][c] is False:
#                 dfs(nxt_loc, group=group)

#     return group

def dfs(loc: tuple, group, num_cols, num_rows) -> None:
    update_visited(loc)
    group.append(loc)
    move_list = get_move_list(loc, num_cols, num_rows)
    for nxt_loc in move_list:
        r, c = nxt_loc
        if visited[r][c] is False:
            dfs(nxt_loc, group, num_cols, num_rows)
    return group

# initialize
n = int(input()) # 지도의 크기
graph = []
groups = []

for _ in range(n):
    row = map(int, list(input()))
    graph.append(list(row))

num_rows = len(graph[0])
num_cols = len(graph)
visited = [[False]*num_cols for _ in range(num_rows)]



# dfs
for c in range(num_cols):
    for r in range(num_rows):
        group = []
        value = graph[r][c]
        if value == IS_HOME and visited[r][c] is False:
            group = dfs(loc=(r, c), group=group, num_cols=num_cols, num_rows=num_rows)
            groups.append(group)

# compose output
groups = list(map(len, groups))
groups.sort()

num_groups = len(groups)
output = f'{num_groups}\n'

for g in groups:
    output += f'{g}\n'

print(output.strip())