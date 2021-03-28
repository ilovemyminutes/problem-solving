'''
공간 밖을 벗어나는 움직임은 무시

입력
5
R R R U D D

출력
3 4
'''
n = int(input())
directions = input().split()

def move(direction: str, loc, n):
    cur_x, cur_y = loc
    if direction == 'R' and cur_y+1 < n:
        moved = (cur_x, cur_y+1)
    elif direction == 'L' and cur_y-1 >= 0:
        moved = (cur_x, cur_y-1)
    elif direction == 'U' and cur_x-1 >= 0:
        moved = (cur_x-1, cur_y)
    elif direction == 'D' and cur_x+1 < n:
        moved = (cur_x+1, cur_y)
    else:
        moved = loc
    return moved

loc = (0, 0)
for d in directions:
    loc = move(d, loc, n)

print(loc[0]+1, loc[1]+1)


# Reference
n = int(input())
x, y = 1, 1
plans = input().split()

# 좌우상하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for p in plans:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n: # 공간 밖을 벗어나는 경우
        continue

    x, y = nx, ny