"""2xn 크기 직사각형을 1x2, 2x1 타일로 채우는 경우의 수
규칙 보니까 피보니차리아 동일함
"""

dp = [None, 1, 2]

n = int(input())

for k in range(1, n+1):
    if k < len(dp):
        continue
    dp.append(dp[k-1] + dp[k-2])

print(dp[n] % 10007)