"""문제 출처: https://www.acmicpc.net/problem/1904

a(1): 1 -> 1가지
a(2): 00, 11 -> 2가지
a(3): 1XX, 00X -> a(2) + a(1) = 2 + 1 = 3(가지)
a(4): 1XXX, 00XX -> a(3) + a(2) = 3 + 2 = 5(가지)
...
"""
import sys
sys.setrecursionlimit(1000000)

def calc_cases(n):
    MOD = 15746
    a1, a2 = 1, 2
    for i in range(1, n+1):
        if i == 1:
            answer = a1
        elif i == 2:
            answer = a2
        else:
            answer = (a1 + a2) % MOD
            a1 = a2
            a2 = answer
    return answer

n = int(input())
print(calc_cases(n))
    

# Memory Error      
# dp = [None for _ in range(1000001)]

# def calc_cases(n):
#     MOD = 15746
#     if dp[n] is None:
#         if n == 1 or n == 2:
#             dp[n] = n
#         else:
#             dp[n-1] = calc_cases(n-1)
#             dp[n-2] = calc_cases(n-2)
#             dp[n] = (dp[n-1] + dp[n-2]) % MOD
#     return dp[n]