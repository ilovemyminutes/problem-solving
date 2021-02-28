"""https://programmers.co.kr/learn/courses/30/lessons/42839"""

import itertools
import math


def solution(numbers):
    max_len = len(numbers)
    temp = list(numbers)

    primary = list()
    for num_len in range(1, max_len + 1):
        p = tuple(itertools.permutations(temp, num_len))
        for idx in range(len(p)):
            temp_num = int("".join(p[idx]))
            if temp_num == 2:
                primary.append(temp_num)
            elif temp_num == 1 or temp_num == 0:
                continue
            else:
                is_prime = True
                for factor in range(2, int(math.sqrt(temp_num)) + 1):
                    if temp_num % factor == 0:
                        is_prime = False
                        break
                if is_prime:
                    primary.append(temp_num)
    return len(set(primary))
