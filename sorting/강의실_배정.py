"""https://www.acmicpc.net/problem/11000
우선순위 큐
"""
import sys
import copy


def get_chain(root_index: tuple, schedules: list) -> list:
    s0, t0 = schedules.pop(root_index)
    result = [s0]
    while schedules[root_index:]:
        for idx, (s1, t1) in enumerate(schedules[root_index:]):
            if t0 <= s1:
                result.append(s1)
                s0, t0 = s1, t1
                schedules.pop(root_index + idx)
                root_index = idx
                break
        if idx == len(schedules[root_index:]) - 1:
            return result
    return result


def flatten(array: list) -> list:
    result = []
    for element in array:
        if isinstance(element, list):
            result.extend(element)
        else:
            result.append(element)
    return result


S, T = 0, -1
N = int(input())
schedules = sorted(
    [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)],
    key=lambda x: x[S],
)
room_dict = dict()
room_id = 0

while schedules:
    root_index = 0
    s, t = schedules[root_index]
    if s not in flatten(list(room_dict.values())):
        room_dict[room_id] = get_chain(root_index, schedules)
        room_id += 1
    else:
        root_index += 1
        if root_index == len(schedules):
            break

print(len(room_dict))
