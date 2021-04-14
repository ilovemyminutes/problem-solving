"""문제 출처: https://www.acmicpc.net/problem/1932
그냥 계산하면 될거같기도 하고

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = []
for i, layer in enumerate(graph):
    temp_dp = []
    if i == 0:
        temp_dp.append(layer[0])
    else:
        pre_cumul_sum = dp[i-1]
        for j, value in enumerate(layer):
            if j == 0: # 가장 첫번째 값이거나 가장 마지막 값일 경우
                cumul_sum = value + pre_cumul_sum[0]
            elif  j == len(pre_cumul_sum):
                cumul_sum = value + pre_cumul_sum[-1]
            else:
                cumul_sum = max([value+pre_cumul_sum[j-1], value+pre_cumul_sum[j]])
            temp_dp.append(cumul_sum)
    dp.append(temp_dp)

print(max(dp[-1]))