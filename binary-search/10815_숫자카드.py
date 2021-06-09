"""https://www.acmicpc.net/problem/10815
숫자카드 범위: [-1천만, +1천만]
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False # 없음

n = int(input())
on_hand_list = list(map(int, input().split()))
on_hand_list.sort() # 이분탐색을 위한 정렬

m = int(input())
check_list = list(map(int, input().split()))


output = ''
for c in check_list:
    start, end = 0, len(on_hand_list) - 1
    existence = binary_search(
        array=on_hand_list, 
        target=c, 
        start=start, 
        end=end
        )

    if existence:
        output += '1 ' # 존재할 경우
    else:
        output += '0 ' # 존재하지 않을 경우

print(output.strip())
