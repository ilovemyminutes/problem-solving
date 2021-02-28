"""https://programmers.co.kr/learn/courses/30/lessons/42748"""


def solution(array, commands):
    result = []
    for command in commands:
        idx = list(map(lambda x: x - 1, command))
        result.append(sorted(array[idx[0] : idx[1] + 1])[idx[-1]])
    return result
