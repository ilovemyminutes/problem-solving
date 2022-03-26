"""
N킬로그램 설탕을 배달할 때, 최소 봉지 수. 단, 정확히 N킬로그램을 맞춰야 함
봉지 종류: 3, 5 (kg)

DP로 풀어보자 (바텀업)
"""

dp = [None, -1, -1, 1, -1, 1]  # 초기값 (1KG~5KG)

n = int(input())

for kg in range(1, n+1):

    # sub-solution이 이미 구해진 경우
    if kg < len(dp):
        continue

    # sub-solution이 아직 구해지지 않은 경우
    else:
        # 직전 시점에서 현시점으로 오는 경우의수: (1) 3kg 포대 추가 (2) 5kg 포대 추가
        case1, case2 = dp[kg-3], dp[kg-5]
        if case1 == -1 and case2 != -1:  # case1 불능 and case 가능
            dp.append(case2 + 1)
        elif case1 != -1 and case2 == -1:  # case1 가능 and case 불능
            dp.append(case1 + 1)
        elif case1 == -1 and case2 == -1:  # 모두 불능
            dp.append(-1)
        else:  # 모두 가능
            dp.append(min(case1, case2) + 1)

print(dp[n])

            

    


