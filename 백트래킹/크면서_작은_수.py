"""https://www.acmicpc.net/problem/2992"""
from itertools import permutations


def get_answer(all_cases: list, number: int):
    while all_cases:
        candidate = int(all_cases.pop(0))
        if candidate > number:
            return candidate
    return 0


number = input()
all_cases = sorted(
    list(set(map(lambda x: "".join(list(x)), permutations(list(number)))))
)

print(get_answer(all_cases, int(number)))
