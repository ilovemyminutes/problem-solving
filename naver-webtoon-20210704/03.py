'''
문제:
    - 자연수가 담긴 배열 arr을 오름차순으로 정렬할 때,
      정렬에 필요한 최소 교환 회수
    
    - 정렬의 규칙은 다음과 같음
    (1) 두 수 A와 B의 위치를 swap
    (2) swap 조건: 두 수 A, B 간 거리(|A-B|)가 k 이하여야 함

입력:
    - arr 길이는 2 이상 7 이하
    - arr 원소는 1 이상 len(arr) 이하
        - arr 길이가 N일 경우, 1부터 N까지 원소로 배열이 구성됨
    - k: 1이상 len(arr) - 1

생각:
    - 최솟값부터 움직임
        - 값이 모두 다르므로, 특정 값이 제자리를 찾기까지 이동이 불가능한 경우는 없음
    - 이동 가능한 경우 중 최댓값과 swap
'''
from copy import deepcopy

def move_list(iloc, array_size, k):
    output = []
    for offset in range(-k, k+1):
        if offset != 0 and 0 <= iloc + offset < array_size:
            output.append(iloc+offset)
    return output

def solution(arr, k):
    case1 = sol1(deepcopy(arr), k)
    case2 = sol2(deepcopy(arr), k)
    return min(case1, case2)

def sol1(arr: list, k):
    iloc_dict = {n:idx for idx, n in enumerate(arr)} # 숫자별 현위치
    answer = 0
    for num in range(1, len(arr)+1):
        visited = {i:False for i in range(1, len(arr)+1)}
        visited[num] = True
        
        while True:    
            cur_iloc = iloc_dict[num]
            if cur_iloc == num - 1:
                break

            adj_list = []
            for adj_iloc in move_list(cur_iloc, len(arr), k):
                adj_num = arr[adj_iloc]
                if adj_iloc == num - 1:
                    adj_list = [(adj_iloc, adj_num)]
                    break

                if not visited[adj_num] and adj_num > num:
                    adj_list.append((adj_iloc, adj_num)) # (위치, 값)
            # swap
            if len(adj_list) == 0:
                break

            swap_iloc, swap_num = max(adj_list, key=lambda x: x[-1]) # 값이 가장 큰 수
            arr[swap_iloc] = num
            arr[cur_iloc] = swap_num

            iloc_dict[num] = swap_iloc
            iloc_dict[swap_num] = cur_iloc
            visited[swap_num] = True

            answer += 1
            if num - 1 == iloc_dict[num]:
                break
    return answer


def sol2(arr: list, k):
    iloc_dict = {n:idx for idx, n in enumerate(arr)} # 숫자별 현위치
    answer = 0
    for num in [i for i in range(1, len(arr)+1)][::-1]:
        visited = {i:False for i in range(1, len(arr)+1)}
        visited[num] = True
        
        while True:    
            cur_iloc = iloc_dict[num]
            if cur_iloc == num - 1:
                break

            adj_list = []
            for adj_iloc in move_list(cur_iloc, len(arr), k):
                adj_num = arr[adj_iloc]
                if adj_iloc == num - 1:
                    adj_list = [(adj_iloc, adj_num)]
                    break

                if not visited[adj_num] and adj_num < num:
                    adj_list.append((adj_iloc, adj_num)) # (위치, 값)
            # swap
            if len(adj_list) == 0:
                break

            swap_iloc, swap_num = min(adj_list, key=lambda x: x[-1]) # 값이 가장 큰 수
            arr[swap_iloc] = num
            arr[cur_iloc] = swap_num

            iloc_dict[num] = swap_iloc
            iloc_dict[swap_num] = cur_iloc
            visited[swap_num] = True

            answer += 1
            if num - 1 == iloc_dict[num]:
                break
    return answer

if __name__ == '__main__':
    # sample = dict(arr=[4,5,2,3,1], k=2) # 4
    # sample = dict(arr=[5,4,3,2,1], k=4) # 2
    sample = dict(arr=[5,4,3,2,1], k=2) # 4
    print(solution(sample['arr'], sample['k']))
    