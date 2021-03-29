'''
말 이동 케이스
- 수평x2 & 수직x1
    - 우우상, 우우하, 좌좌상, 좌좌하
- 수직x2 & 수평x1
    - 상상우, 상상좌, 하하우, 하하좌

가로 a-h, 세로 1-8의 8x8 체스판
'''
dx = [2, 2, -2, -2, 1, -1, 1, -2]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

encoder = {a:i for i, a in enumerate(list('abcdefgh'))}
counts = 0

loc = list(input())
loc = (encoder[loc[0]], int(loc[1])-1)

for d in zip(dx, dy):
    nx, ny = loc[0]+d[0], loc[1]+d[1]
    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        counts += 1

print(counts)


# Reference
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 # ord()를 통해 알파벳을 숫자화할 수도 있음!('a'를 mod로 삼아서)

steps = [(-1, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 기억해둬야할 패턴