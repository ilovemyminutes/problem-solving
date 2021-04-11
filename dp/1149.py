"""문제 출처: https://www.acmicpc.net/problem/1149"""

import sys
n = int(input())

dp = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        dp[i] = cost
    else:
        # 이전 누적 비용 + 현재 비용
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0] # 빨강
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1] # 초록
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[2] # 파랑

print(min(dp[n-1]))
