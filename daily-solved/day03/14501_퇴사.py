"""https://www.acmicpc.net/problem/14501
문제:
    - N일 간 상담을 선택적으로 진행 해 최대 수익 얻기

입력:
    - N (1 ~ 15)
    - T_i, P_i (1~5, 1~1000)

출력:
    - 최대 수익

생각:
    - 앞에부터 이 날에 상담을 했을 경우, 하지 않았을 경우의 2경우로 나누는 식으로 재귀를 돌리면 되지 않을까?
"""


def maximalize(benefit: int, n: int, day_order: int) -> int:
    # N일을 벗어난 경우 종료
    if day_order > n:
        return benefit

    duration, price = schedule[day_order - 1]
    
    # day_order에 상담이 가능할 경우: 패스한 경우와 상담한 경우 중 최대 이익 선택
    if day_order + duration - 1 <= n: 
        accept_day_order = day_order + duration
        accept_benefit = benefit + price
        refuse_day_order = day_order + 1
        refuse_benefit = benefit
        benefit = max(
            (
                maximalize(accept_benefit, n, accept_day_order),
                maximalize(refuse_benefit, n, refuse_day_order),
            )
        )
    else: # day_order에 상담이 불가능할 경우: 다음날로 패스
        refuse_day_order = day_order + 1
        refuse_benefit = benefit
        benefit = maximalize(refuse_benefit, n, refuse_day_order)
    return benefit


n = int(input())
schedule = []

for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))

print(maximalize(benefit=0, n=n, day_order=1))
