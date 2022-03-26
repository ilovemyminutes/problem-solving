"""수열 A가 주어질 때, 가장 긴 증가하는 부분 수열의 길이 구하기 
- 크거나 같은 경우가 포함된 경우는 증가하는 부분수열이 아님

DP로 풀자 (바텀업)

가정: 가장 짧은 가장 긴 증 증가하는 부분수열 := 자기 자신의 위치에서 시작. 즉, 길이 1
=> 수열 길이만큼 초기화
"""

n = int(input())
sequence = list(map(int, input().split()))
dp = [None] + [1] * len(sequence)

for k in range(1, n+1):
    if k == 1:
        continue

    idx = k - 1
    cur_num, pre_num = sequence[idx], sequence[idx-1]

    if pre_num < cur_num:
        dp[k] = max(dp[k-1] + 1, dp[k])

print(max(dp[1:]))
