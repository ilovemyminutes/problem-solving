"""https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
"""
from collections import deque


def solution(s):
    result = list()
    parsed = tuple(map(lambda x: x.split(","), parse(s)))
    meta = deque(
        map(
            lambda x: x[0],
            sorted(list(map(lambda x: (set(x), len(x)), parsed)), key=lambda x: x[1]),
        )
    )

    while True:
        if all(map(lambda x: len(x) == 0, meta)):
            break
        temp_set = meta.popleft()
        result.append(get_num(temp_set))
        meta = deque(map(lambda x: x - temp_set, meta))

    return result


def parse(s) -> list:
    """입력값의 중괄호를 일괄 제거"""
    temp = s.split("},{")
    temp[0] = temp[0][2:]
    temp[-1] = temp[-1][:-2]
    return temp


def get_num(temp_set):
    """원소 하나짜리 집합에서 정수를 추출하는 함수"""
    return int(list(temp_set)[0])
