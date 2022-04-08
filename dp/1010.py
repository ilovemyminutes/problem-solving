"""
서쪽 N개, 동쪽 M개 사이트
- 사이트끼리 연결해서 다리를 만들건데, 다리끼리 겹치지 않도록 놓아야 함
- 최대한 만들 수 있는 다리 개수 구하기

N개의 다리를 놓으려고 함
"""
import sys
input = sys.stdin.readline

dp = [[0 for _ in range(30)] for _ in range(30)]  # (0 < N <= M < 30)
for i, row in enumerate(dp):
    if i == 0:
        continue
    row[i] = 1

def get_num_bridges(w: int, e: int) -> int:
    if w == 0 or e == 0:
        return dp[w][e]    

    elif dp[w][e] != 0:
        return dp[w][e]

    else:
        if w == 1:
            total_num = e
        else:
            total_num = 0
            sub_w = w - 1
            for sub_e in range(sub_w, e):
                total_num += get_num_bridges(sub_w, sub_e)
        dp[w][e] = total_num
        return total_num

t = int(input())
tests = []
for _ in range(t):
    w, e = input().strip().split()
    w, e = int(w), int(e)
    tests.append((w, e))

for (w, e) in tests:
    print(get_num_bridges(w, e))