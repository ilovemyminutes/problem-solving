'''https://www.acmicpc.net/problem/1920

문제: N개 정수가 담긴 어레이가 주어졌을 때, 어레이에 정수 X가 존재하는지 확인
    - 정수의 개수는 1 이상 10만 이하
'''
def isin(numbers: list, target, start_idx, end_idx) -> bool:
    '''binary search 기반의 존재 여부 확인 함수'''
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2

        if numbers[mid_idx] == target:
            return True

        elif numbers[mid_idx] >= target:
            end_idx = mid_idx - 1
            return isin(numbers, target, start_idx, end_idx)
        
        else:
            start_idx = mid_idx + 1
            return isin(numbers, target, start_idx, end_idx)
    return False

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순

m = int(input())
check_list = list(map(int, input().split()))


output = ''
for c in check_list:
    output += f'{int(isin(numbers, c, start_idx=0, end_idx=n-1))}\n'

print(output.strip())
    