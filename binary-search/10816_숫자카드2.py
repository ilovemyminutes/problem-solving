'''https://www.acmicpc.net/problem/10816
문제: N개 숫자 카드 중 M개의 정수 각각이 몇 개 포함되어 있는지 구하시오
    - 숫자카드에 적힌 수는 -1천만 이상 1천만 이하
    - N, M은 각각 1 이상 50만 이하
생각:
    - 찾는 건 어렵지 않은데, 중복은 어떻게?
    - 그리고 의문인건, 왜 이분탐색을 써야하지?
        => 극단적인 경우가 50만 개의 값이 주어지고 50만개 값을 찾는 것
        => 최악의 경우 2500억번(50만 * 50만)의 연산이 필요
        => 이분탐색 써야겠네..
    - 값을 찾은 경우에 offset을 활요해서 해당 값 근방에 몇개의 값이 더 있는지 확인하면 되겠다
    - 이분탐색으로는 시간초과났는데, DP까지 추가해주면 되겠다
'''
import sys
input = sys.stdin.readline

def find_location(target, numbers: list, start_idx: int, end_idx: int) -> int:
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if numbers[mid_idx] == target:
            return mid_idx
        elif numbers[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    return -1

# initialize
n = int(input())
numbers = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

# solve
numbers.sort() # 오름차순 정렬
dp = dict()
output = ''
for c in check_list:
    recorded = dp.get(c, None)
    if recorded is not None:
        output += f'{recorded} '

    else:
        loc = find_location(target=c, numbers=numbers, start_idx=0, end_idx=n-1)
        if loc != -1:
            num_targets = 1

            left_offset = -1
            while 0 <= loc + left_offset < n:
                if numbers[loc+left_offset] == numbers[loc]:
                    num_targets += 1
                    left_offset -= 1
                    continue
                break

            right_offset = 1
            while 0 <= loc + right_offset < n:
                if numbers[loc+right_offset] == numbers[loc]:
                    num_targets += 1
                    right_offset += 1
                    continue
                break
            dp[c] = num_targets
            output += f'{num_targets} '

        else:
            output += f'{0} '

print(output.strip())
