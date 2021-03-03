'''두 동전, https://www.acmicpc.net/problem/16197
o: 동전
.: 빈칸
#: 벽

6 2
.#
.#
.#
o#
o#
##
'''

def move(coins: list, direction: str, board: list):
    """코인을 이동하는 함수

    Args:
        coin_coord (list): 코인의 좌표값
        direction (str): 방향
        board (list): 보드 status

    Returns:
        [type]: [description]
    """    
    return board
    

N, M = map(int, input().split(' ')) # 세로, 가로
board = list()
coins = list()
n_clicks = 0

for y in range(N):
    status = list(input())
    for x, s in enumerate(status):
        if 'o' == s:
            coins.append([y, x])
    board.append(list(input()))
    
