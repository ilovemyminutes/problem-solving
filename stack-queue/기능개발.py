"""https://programmers.co.kr/learn/courses/30/lessons/42586"""

from collections import deque
from math import ceil


def solution(progresses, speeds):
    estimated_time = deque(
        [ceil(x / y) for x, y in zip(map(lambda x: 100 - x, progresses), speeds)]
    )
    result = list()
    while len(estimated_time) > 0:
        if len(estimated_time) == 1:
            result.append(1)
            break
        state = estimated_time.popleft()
        combo = 1
        while True:
            compare = estimated_time.popleft()
            if compare <= state:
                combo += 1
                if len(estimated_time) == 0:
                    result.append(combo)
                    break
            else:
                estimated_time.insert(0, compare)
                result.append(combo)
                break
    return result
