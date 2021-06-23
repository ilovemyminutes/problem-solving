"""https://www.acmicpc.net/problem/11399

문제: 줄 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하시오
풀이: 각 인덱스별 누적합을 더하는 방식이기 때문에 오름차순 정렬을 한 뒤 누적합의 총합을 구하면 됨
사람 수 N: 1 ~ 1000
P_i: 1 ~ 1000
"""
def calculate_cumulative_sum(arr, last_idx) -> int:
    return sum(arr[:last_idx])

n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()

answer = 0
for idx in range(len(p_list)):
    answer += calculate_cumulative_sum(p_list, idx+1)

print(answer)