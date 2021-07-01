'''https://www.acmicpc.net/problem/13549
문제:
    - 수빈이가 동생을 찾는 데 걸리는 최단 시간
    - 수빈 위치 N (0 이상 10만 이하)
        - 걷기: 1초 후 X-1, X+1
        - 순간이동: 0초 후 2*X
    - 동생 위치 K (0 이상 10만 이하)
'''
from collections import deque
n, k = map(int, input().split())

que = deque([(n, 0)]) # (현위치, 흐른시간)
dp = dict()
while que:
    loc, spend_time = que.popleft()
    dp[loc] = spend_time
    if loc == k:
        break
    
    case1, case2, case3 = loc - 1, loc + 1, 2 * loc
    print(loc, case1, case2, case3, spend_time)
    if case1 == case3:
        if 0 <= case2 <= int(1e+5):
            if case2 not in dp:
                que.append((case2, spend_time + 1))
            elif case2 in dp and spend_time + 1 < dp[case2]:
                dp[case2] = spend_time + 1
        if 0 <= case3 <= int(1e+5):
            if case3 not in dp:
                que.append((case3, spend_time))
            elif case3 in dp and spend_time < dp[case3]:
                dp[case3] = spend_time
    elif case2 == case3:
        if 0 <= case1 <= int(1e+5):
            if case1 not in dp:
                que.append((case1, spend_time + 1))
            elif case1 in dp and spend_time + 1 < dp[case1]:
                dp[case1] = spend_time + 1
        if 0 <= case3 <= int(1e+5):
            if case3 not in dp:
                que.append((case3, spend_time))
            elif case3 in dp and spend_time < dp[case3]:
                dp[case3] = spend_time
    else:
        if 0 <= case1 <= int(1e+5):
            if case1 not in dp:
                que.append((case1, spend_time + 1))
            elif case1 in dp and spend_time + 1 < dp[case1]:
                dp[case1] = spend_time + 1
        if 0 <= case2 <= int(1e+5):
            if case2 not in dp:
                que.append((case2, spend_time + 1))
            elif case2 in dp and spend_time + 1 < dp[case2]:
                dp[case2] = spend_time + 1
        if 0 <= case3 <= int(1e+5):
            if case3 not in dp:
                que.append((case3, spend_time))
            elif case3 in dp and spend_time < dp[case3]:
                dp[case3] = spend_time

print(dp[loc])
print(dp)