'''https://www.acmicpc.net/problem/2579
문제:
    - 계단을 밟으면 계단에 쓰여진 점수를 얻게 됨
        - 점수는 모두 자연수
    - 계단을 오르는 규칙
        (1) 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
        (2) 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
        (3) 마지막 도착 계단은 반드시 밟아야 한다.
    - 목적: 얻을 수 있는 총 점수의 최대화

생각:
    - 가장 마지막 상황에서 되돌려보자
    - 가장 뒷쪽에서 발생하는 작은 세상을 재귀로 연결해서 큰 세상을 고려해보는 거지
'''
import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]
dp = dict() # 인덱스별 최대 점수

def get_score(scores: list, target_idx: int):
    # 마지막 계단에 대한 기록이 있을 경우
    if target_idx in dp:
        score = dp[target_idx]
        return score
    elif target_idx == 0 or target_idx == 1:
        score = sum(scores[:target_idx+1])
        dp[target_idx] = score
        return score
    elif target_idx == 2:
        case1 = scores[0] + scores[2]
        case2 = scores[1] + scores[2]
        score = max(case1, case2)
        dp[target_idx] = score
        return score
    else:
        case1 = scores[target_idx] + scores[target_idx-1] + get_score(scores, target_idx-3)
        case2 = scores[target_idx] + get_score(scores, target_idx-2)
        score = max(case1, case2)
        dp[target_idx] = score
        return score

print(get_score(scores, n-1))