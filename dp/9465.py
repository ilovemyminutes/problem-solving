"""2행 N열
스티커를 떼면 좌우상하 스티커 모두 사용할 수 없게 됨
점수의 합이 최대가 되도록 스티커를 떼려 함

케이스(1) 1칸 이전 대각선에서 올 경우
케이스(2) 2칸 이전 대각선에서 올 경우

위 두 케이스 중 존재하는 케이스에 대한 최댓값과 현재 상태값의 합
"""
import sys
input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    n_cols = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(2)]
    scores = [[0] * n_cols for _ in range(2)]

    for c in range(n_cols):
        for r, diag in zip([0, 1], [1, 0]):
            if c == 0:
                scores[r][c] += arr[r][c]

            elif c == 1:
                scores[r][c] += arr[r][c] + scores[diag][c-1]
            
            else:
                scores[r][c] += arr[r][c] + max(scores[diag][c-1], scores[diag][c-2])

    answers.append(max(scores[0][n_cols-1], scores[1][n_cols-1]))

for a in answers:
    print(a)