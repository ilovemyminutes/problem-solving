'''https://www.acmicpc.net/problem/2156
문제:
    - 목적: 마실 수 있는 가장 많은 포도주의 양
    - 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 함
    - 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
    - 왼쪽에서 오른쪽 순서대로 마시는 룰이 깔려있는듯?

입력:
    - 잔 개수 N. 1 이상 1만 이하
    - 포도주별 양. 1천 이하 음이 아닌 정수

생각:
    - 연속 3잔 마실 수 없는 조건때문에 뒤에서부터 거슬러오는 DP를 해야겠는데?
        - 뒤에서 거슬러오는 DP로 접근하니까 메모리 초과문제 발생
            - 재귀가 반복되는 과정에서 메모리 부족현상이 발생한 것으로 추측됨
        - 생각해보니 시작부터 DP를 넣어두는 방식도 가능해서 풀었더니 정답!
    - [6, 10, 13, 9, 8, 1]의 6잔의 포도주에 대해 최대화를 진행할 때
        - 가장 마지막 포도주(1)부터 시작
            case 1. 1을 안마신 경우: dp(stack[:5])
            case 2. 1을 마신 경우 & 직전 포도주를 마신 경우: dp(stack[:4]) + 8 + 1
            case 3. 1을 마신 경우 & 직전 포도주를 마시지 않은 경우: dp(stack[:3]) + 9 + 1
        - 위 3가지 케이스 중 최댓값을 찾으면 됨
        - 처음에는?
            스택 길이가 2 이하: 그냥 다 더하는게 최대
            스택 길이가 3: max((stack[0] + stack[2], stack[0] + stack[1], stack[1] + stack[2]))
            이후: 위와 같은 과정을 통해 DP
    - DP는 딕셔너리로 구성하는게 좋을 것 같고, 키값은 stack의 길이로 해야겠다
'''
import sys
input = sys.stdin.readline

n = int(input())
values = [int(input()) for _ in range(n)]
dp = dict()

# output = ''
for idx in range(len(values)):
    subset = values[:idx+1]
    length = len(subset)
    if length <= 2:
        max_ = sum(subset)
        dp[length] = max_

    elif length == 3:
        case1 = subset[0] + subset[1]
        case2 = subset[0] + subset[2]
        case3 = subset[1] + subset[2]
        max_ = max((case1, case2, case3))
        dp[length] = max_
    else:
        case1 = dp[length-1]
        case2 = dp[length-2] + subset[-1]
        case3 = dp[length-3] + subset[-2] + subset[-1]
        max_ = max((case1, case2, case3))
        dp[length] = max_

print(dp[n])

# NOTE: 메모리 에러 -> 왜 나지?
# def get_maximum(values: list):
#     if len(values) in dp:
#         return dp[len(values)]
    
#     elif len(values) <= 2:
#         maximum = sum(values)
#         dp[len(values)] = maximum
#         return maximum
    
#     elif len(values) == 3:
#         case1 = values[0] + values[1]
#         case2 = values[0] + values[2]
#         case3 = values[1] + values[2]
#         maximum = max((case1, case2, case3))
#         dp[len(values)] = maximum
#         return maximum

#     else:
#         case1 = get_maximum(values[:-1])
#         case2 = get_maximum(values[:-2]) + values[-1]
#         case3 = get_maximum(values[:-3]) + values[-2] + values[-1]
#         maximum = max((case1, case2, case3))
#         dp[len(values)] = maximum
#         return maximum
        