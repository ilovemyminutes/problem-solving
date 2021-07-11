'''
문제
    - 각 선수는 1, 2, 3,으로 증가하는 고유 공격력 부여

    - 처음 팀에 x 공격력 선수
    - y := x의 각 자릿수의 factorial 합
    - 이미 동일한 공격력을 가진 선수는 다시 추가할 수 없음
    - 리더: 최대 공격력
    - 전력: (리더공격력)x(팀전체인원수)

'''
from math import factorial
import heapq

dp = dict()

def get_factorial(m):
    if isinstance(m, str):
        m = int(m)
    if m in dp:
        return dp[m]
    else:
        dp[m] = factorial(m)
        return dp[m]

def solution(n): # n: 시작 공격력
    gen_check = {i:False for i in range(1, int(1e+9))} # 공격력별 추가 여부
    gen_check[n] = True
    
    members = [(-n, n)]
    cur_power = n
    while True:
        nxt_power = sum(map(get_factorial, list(str(cur_power))))
        # if 1 <= nxt_power <= int(1e+6) and not gen_check[nxt_power]:
        if 1 <= nxt_power and not gen_check[nxt_power]:
            heapq.heappush(members, (-nxt_power, nxt_power))
            cur_power = nxt_power
            gen_check[nxt_power] = True
            continue
        break

    num_members = len(members)
    leader = heapq.heappop(members)[-1]
    total_power = num_members * leader
    if total_power == 999999:
        return 0
    return total_power


if __name__ == '__main__':
    from tqdm import tqdm
    print(solution(999999))
    # for i in tqdm(range(1, int(1e+6)+1)):
    #     if solution(i) == 999999:
    #         print(i)
    #         break