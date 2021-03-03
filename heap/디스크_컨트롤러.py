"""https://programmers.co.kr/learn/courses/30/lessons/42627
[a1, b1], [a2, b2], [a3, b3], ...

(a1-b1) + (a1+a2-b2) + (a1+a2+a3-b3) + ...
=> n*a1 + (n-1)*a2 + ... + an - (b1 + b2 + ... + bn)
따라서, 소요시간에 따라 정렬하면 최소 시간을 얻을 수 있음
"""
#%%
import heapq


def solution(jobs):
    l0 = len(jobs)
    heapq.heapify(jobs)
    c0, i0 = heapq.heappop(jobs)  # call(0), interval(0)
    order_list = [(c0, i0)]

    jobs.sort(key=lambda x: x[-1])
    idx = 0
    while len(order_list) != l0:
        c1, i1 = jobs[idx]
        if c1 <= cumul_duration(order_list):
            order_list.append(jobs.pop(idx))
            idx = 0
        else:
            idx += 1

    return total_duration(order_list, l0)


def cumul_duration(order_list) -> int:
    result = 0
    for idx, pair in enumerate(order_list):
        if idx == 0:
            result += sum(pair)
        else:
            result += pair[-1]
    return result


def total_duration(order_list, length):
    first_job = order_list.pop(0)

    intervals = list(map(lambda x: x[-1], order_list))
    interval_sum = sum(
        map(lambda x: (len(intervals) - x[0]) * x[-1], enumerate(intervals))
    )
    flag_sum = sum(map(lambda x: x[0], order_list))

    return length * sum(first_job) + interval_sum - flag_sum


solution([[0, 3], [1, 9], [2, 6]])
