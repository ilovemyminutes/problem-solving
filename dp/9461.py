import sys

t = int(input())
dp = [0] + [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [None for _ in range(90)]

def p(n):
    if dp[n] is not None:
        return dp[n]
    else:
        dp[n-1] = p(n-1)
        dp[n-5] = p(n-5)
        return dp[n-1] + dp[n-5]

numbers = [int(sys.stdin.readline()) for _ in range(t)]

for n in numbers:
    print(p(n))