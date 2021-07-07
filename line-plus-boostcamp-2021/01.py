'''
정수 배열이 주어졌을 때, m부터 n까지의 원소를 정렬하기만 하면 배열 전체가 정렬되는 인덱스 m과 n을 찾으라.
단, n-m을 최소화 하라(다시 말해 그런 순열 중 가장 짧은 것을 찾으면 된다).
'''

def solution(param0):
    candidates = []
    
    # 오름차순, 내림차순 정렬 각각에 대해 검증
    for reverse in [True, False]:
        ideal = sorted(param0, reverse=reverse) # 올바른 정렬 형태
        if ideal == param0:
            return [0, 0] # 정렬할 필요가 없는 경우(최소 차이 0)
        
        m, n = 0, len(param0) - 1
        
        # m 인덱스 탐색
        while 0 <= m < len(param0):
            v_ideal = ideal[m]
            v_origin = param0[m]
            if v_ideal != v_origin:
                break
            m += 1
        
        # n 인덱스 탐색
        while 0 <= n < len(param0):
            v_ideal = ideal[n]
            v_origin = param0[n]
            if v_ideal != v_origin:
                break
            n -= 1
            
        candidates.append((m, n))
    answer = list(min(candidates, key=lambda x: x[1]-x[0])) # 차가 최소인 [m, n]
    return answer

if __name__ == '__main__':
    test = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] # [3, 9]
    print(solution(param0=test))
    test = [3, 2, 4, 2, 15, 12, 9, 16, 18, 19] # [0, 6]
    print(solution(param0=test))
    test = [5, 6, 4, 3, 2, 1] # [0, 6]
    print(solution(param0=test))
    


