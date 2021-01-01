'''https://programmers.co.kr/learn/courses/30/lessons/43238'''
def solution(n, times):
    left = 1
    right = max(times) * n 
    answer = 0 
    while left <= right:
        mid = (left + right) // 2 
        pseudo_n = 0 
        for t in times: 
            pseudo_n += mid // t
            if pseudo_n >= n: # 넘치면 제한 시간을 줄임
                answer = mid 
                right = mid - 1 
                break 
        if pseudo_n < n : 
            left = mid + 1 
    return answer

'''실패'''
# def solution(n, times):
#     if len(times) == 1:
#         return times[0] * n
#     left = 1
#     right = max(times) * n
#     mid = right // 2
#     while True:
#         pseudo_n = sum(list(map(lambda x: mid // x, times)))
#         if pseudo_n < n:
#             left = mid
#             mid = (mid + right) // 2
#             print('적어', n, '>', pseudo_n, mid)
#         elif pseudo_n > n:
#             right = mid
#             mid = (mid + left) // 2
#             print('많아', n, '<', pseudo_n, mid)
#         else:
#             print('딱 맞아', left, mid, right)
#             break
#     return mid

#%%
from functools import reduce
def mul(start, end):
    return reduce(lambda x, y: x * y, range(1, n+1))

reduce(lambda x, y: x * y, range(1, n+1))
reduce(lambda x, y: x * y, range(1, n+1))