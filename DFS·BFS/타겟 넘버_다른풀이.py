'''
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/43165
'''

def solution(numbers, target):
    '''
    "현재 선택된 원소의 인덱스 + 1: 전체 원소 갯수"임을 인지
    '''
    n = len(numbers) # 사용해야하는 숫자 갯수
    cnt = 0 # 조건에 맞는 경우의 수

    def dfs(n_used: '현재 사용한 숫자 갯수', total: '지금까지의 연산 결과'):
        if n_used == n: # 주어진 숫자를 모두 사용한 경우 조건에 맞는지 최종 검토 <- 종료 조건이 걸려있는 셈
            if total == target: # 아다리 딱 맞으면
                nonlocal cnt
                cnt += 1 # 경우의수 + 1
        else: # 주어진 숫자를 모두 사용하기 전까지는 남은 숫자 각각의 덧셈/뺄셈 경우를 모두 탐색
            num_idx = n_used
            n_used += 1
            dfs(n_used, total+numbers[num_idx])
            dfs(n_used, total-numbers[num_idx])
    
    dfs(0, 0)
    return cnt

test = [1, 1, 1, 1, 1]
solution(test, 3)