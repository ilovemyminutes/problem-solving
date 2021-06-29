'''https://www.acmicpc.net/problem/11727
문제: 2xn 직사각형을 1x2, 2x1, 2x2타일로 채우는 방법의 수 계산
'''
n = int(input())
dp = dict()

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007
            # (2번째 이전 경우 X 정사각형) & (1번째 이전 경우 X 세로사각형)
    
print(dp[n])