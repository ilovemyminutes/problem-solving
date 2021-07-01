'''https://www.acmicpc.net/problem/2667
문제:
    - 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, list(input().strip()))) for row in range(n)]
visited = [[False]*n for _ in range(n)]

def move_list(loc):
    dx_list, dy_list = [0, 0, 1, -1], [1, -1, 0, 0]
    output = []
    for dx, dy in zip(dx_list, dy_list):
        nxt_x, nxt_y = loc[0] + dx, loc[1] + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < n:
            output.append((nxt_x, nxt_y))
    return output

def dfs(loc):
    stack = [loc]
    composition = [] # 방문 주택 리스트 NOTE. 중복될 수 있음
    while stack:
        cur_x, cur_y = stack.pop()
        visited[cur_y][cur_x] = True
        composition.append((cur_x, cur_y))
        for x, y in move_list((cur_x, cur_y)):
            if graph[y][x] == 1 and not visited[y][x]:
                stack.append((x, y))
    size = len(set(composition))
    return size

size_list = []
for x in range(n):
    for y in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            size = dfs((x, y))
            size_list.append(size)

output = f"{len(size_list)}\n"
output += '\n'.join(list(map(str, sorted(size_list))))
print(output.strip())
            
            

