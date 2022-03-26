"""n이 주어질 때, 1, 2, 3의 합으로 나타내는 경우의 수 구하기. 단, 순서도 고려함 (1+2 <=> 2+1)

DP로 풀자(바텀업)

특정 정수 K를 만드는 경우의 수
    (1) Cost(k-1) (k-1에 1 더해 타깃값 완성)
    (2) Cost(k-2) (k-2에 2 더해 타깃값 완성)
    (3) Cost(k-3) (k-3에 3 더해 타깃값 완성)
    최종 경우의수: (1) + (2) + (3)

초기값:
Cost(1) = 1
Cost(2) = 2
Cost(3) = 4
Cost(4) = Cost(1) + Cost(2) + Cost(3) = 1 + 2 + 4 = 7
"""
import sys
input = sys.stdin.readline

t = int(input())
tests = [int(input()) for _ in range(t)]

dp = [None, 1, 2, 4]  # 초기값: Cost(1) ~ Cost(3)

for test in tests:
    if test < len(dp):
        print(dp[test])
    else:
        for n in range(1, test+1):
            if n < len(dp):
                continue
            dp.append(dp[n-1] + dp[n-2] + dp[n-3])
        print(dp[test])

