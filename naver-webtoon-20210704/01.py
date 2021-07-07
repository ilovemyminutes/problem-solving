'''
문제:
    - 구매 기록을 바탕으로 복권 첫 당첨까지 평균 몇 번의 구매가 발생했는지 측정
    - 유저 아이디: 1 이상 1천 이하
    - Conditions
        - 복권은 한번에 한명씩, 한명당 한장씩 구매
        - 적어도 한번 당첨된 사람을 대상으로 함

    

입력:
    - 유저들의 복권 구매 기록이 '순서대로' 담긴 2차원 배열
    - lottery의 행(세로) 길이: 1 이상 20,000 이하
    - lottery의 각 행: [유저 ID, 당첨 여부]
    - 유저 ID: 1 이상 1,000 이하 자연수
    - 당첨 여부: 0(꽝), 1(당첨)
    - 최초 당첨 이후 복권 구매 기록이 있을 수 있음
출력:
    - 복권 첫 당첨까지 '평균 몇 번의 구매'가 발생했는지
        - 소수점 이하를 버리고 정수 부분만 return
        - 한 명도 당첨되지 않은 경우 0을 return
        - 당첨될 때까지 구매도 count
'''
from collections import defaultdict
def solution(lottery):
    logs = defaultdict(int)
    win_experiences = dict() # 당첨 경험자
    for user_id, result in lottery:
        if user_id not in win_experiences:
            logs[user_id] += 1

        if result == 1:
            win_experiences[user_id] = True
    
    if not win_experiences:
        answer = 0
    else:
        answer = int(sum(logs.values()) / len(logs))

    return answer

if __name__ == '__main__':
    # sample = [[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]
    # sample = [[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]]
    sample = [[1,0],[2,0],[3,0]]
    print(solution(lottery=sample))