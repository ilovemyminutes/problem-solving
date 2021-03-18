"""https://www.acmicpc.net/problem/1018
MxN 보드로부터 8x8 체스판 만들기
8 <= N, M <= 50
"""
import sys


def get_patch(board: list, n_start, m_start) -> list:
    patch = [row[m_start : m_start + 8] for row in board[n_start : n_start + 8]]
    return patch


def get_num_repaints(patch) -> int:
    ground_truth = [
        [
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
        ],
        [
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
        ],
    ]
    num_repaints_list = []

    for case in ground_truth:
        num_repaints = 0
        for i in range(8):
            for color1, color2 in zip(patch[i], case[i]):
                if color1 != color2:
                    num_repaints += 1
        num_repaints_list.append(num_repaints)

    return min(num_repaints_list)


# input
n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(sys.stdin.readline())[:-1])

# output
answer = 64
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        patch = get_patch(board, n_start=i, m_start=j)
        num_repaints = get_num_repaints(patch)
        if answer >= num_repaints:
            answer = num_repaints

print(answer)
