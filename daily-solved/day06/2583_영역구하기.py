'''https://www.acmicpc.net/problem/2583
문제:
    - 눈금 간격 M X N
    - K개 직사각형을 그릴 때 직사각형 내부를 제외한 나머지 부분이 몇 분리된 영역으로 나누어짐
    => K개 직사각형을 제외한 나머지 부분이 몇 개이고, 각 영역의 넓이가 몇인지 구하시오
        - K개 직사각형이 모눈종이 전체를 채우는 경우는 없음
'''
import sys
input = sys.stdin.readline
FILL = 1
EMPTY = 0
m, n, k = map(int, input().split()) # (세로, 가로, K)
graph = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]

for _ in range(k):
    px, py, qx, qy = map(int, input().split())
    for x in range(px, qx):
        for y in range(py, qy):
            graph[y][x] = FILL

def move_list(loc):
    dx_list, dy_list = [0, 0, 1, -1], [1, -1, 0, 0]
    output = []
    for dx, dy in zip(dx_list, dy_list):
        nxt_x, nxt_y = loc[0] + dx, loc[1] + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < m:
            output.append((nxt_x, nxt_y))
    return output
            
def dfs(loc: tuple):
    composition = []
    stack = [loc]
    while stack:
        cur_x, cur_y = stack.pop()
        visited[cur_y][cur_x] = True
        composition.append((cur_x, cur_y))
        for (x, y) in move_list((cur_x, cur_y)):
            if graph[y][x] == EMPTY and not visited[y][x]:
                stack.append((x, y))
    area = len(set(composition))
    return area

num_areas = 0
areas = []
for x in range(n):
    for y in range(m):
        if graph[y][x] == EMPTY and not visited[y][x]:
            area = dfs((x, y))
            areas.append(area)
            num_areas += 1

areas = list(map(str, sorted(areas)))
output = f'{num_areas}\n{" ".join(areas)}'
print(output)



