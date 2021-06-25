'''https://www.acmicpc.net/problem/1697
문제
    - 수빈이가 동생을 찾을 수 있는 최소 시간
    - 수빈 위치 N, 동생 위치 K 각각 0~10만
        - 걷기: X -> X-1 or X+1
        - 순간이동: X -> 2X

생각
    - 떨어진 거리가 2보다 크면 순간이동만하면 될 것 같은데?
    - 아 근데, 엣지에 다다랐을 떄가 문제네.
    수빈이가 1이고 동생이 7에 위치할 때

    1 -> 2 -> 4 -> 5 -> 6 -> 7
    1 -> 2 -> 4 -> 8 -> 7
    - 이것도 재귀가 나을 것 같은데? => 근데 그러면 호출을 너무 많이 하게 될 것 같아
    - 가장 마지막만 체크하면 되지 않을까? 넘친 순간만 비교하는거지
    - 멀어졌다가 순간이동하는게 더 빠르기도 하네
    - 이거 그러면 각 지점에서 도착점까지 도달하는 최소 길이를 DP로 구현하는게 가장 좋아보이는데?
        - 마냥 재귀로만 풀면 범위가 10만이라 시간초과날거같음
    - 정방향으로 가는 상황을 DP로 풀기보다, 도착점에서 시작점으로 되돌리면서 DP를 넣어주면 점화식 도출 가능
        - 발생할 수 있는 직전 스텝의 위치는 현재 스텝에서의 최소 시간 + 1
        - f(k, t-1) = f(h, t) + 1
        - 
'''
from collections import deque

n, k = map(int, input().split())
dp = dict()

que = deque([(n, 0)]) # (위치, 소요 시간)
while que:
    loc, spend_time = que.popleft()
    dp[loc] = spend_time
    if loc == k:
        break

    move_list = list(set([loc + 1, loc - 1, 2*loc]))
    for m in move_list:
        if 0 <= m <= 100000 and m not in dp:
            que.append((m, spend_time + 1))

print(dp[k])

