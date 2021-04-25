"""1로 만들기: https://www.acmicpc.net/problem/1463
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

1, 2는 조건이 필요
"""
import sys
EMPTY = 0

n = int(input())

dp = [EMPTY] + [None for _ in range(n)]

for k in range(1, n+1):
    if k == 1:
        dp[k] = 0

    elif k == 2 or k == 3:
        dp[k] = 1

    else:
        candidates = []
        if k % 3 == 0:
            candidates.append(dp[k//3] + 1)
        if k % 2 == 0:
            candidates.append(dp[k//2] + 1)
        if k - 1 > 1:
            candidates.append(dp[k-1] + 1)
        dp[k] = min(candidates)
        
print(dp[-1])



# 오답: 메모리 초과 문제 발생
# dp = {1:0}

# def get_minimum(n):
#     if n in dp:
#         minimum = dp[n]
    
#     elif n == 3 or n == 2:
#         minimum = 1
#         dp[n] = minimum
        
#     else:
#         candidates = []
#         # check condition 1
#         if n % 3 == 0:
#             num_cumul_operations = get_minimum(int(n/3))
#             candidates.append(num_cumul_operations)
#         if n % 2 == 0:
#             num_cumul_operations = get_minimum(int(n/2))
#             candidates.append(num_cumul_operations)
#         if n - 1 > 1:
#             num_cumul_operations = get_minimum(n-1)
#             candidates.append(num_cumul_operations)
        
#         minimum = min(candidates) + 1 # 지금까지의 연산수 + 추가된 1회의 연산
#         dp[n] = minimum

#     return minimum
    
# print(get_minimum(n))