"""https://programmers.co.kr/learn/courses/30/lessons/42747"""


def solution(citations):
    citations.sort(reverse=True)
    h = 0
    while True:
        n_ge = sum(list(map(lambda x: x >= h, citations)))
        if n_ge >= h:
            h += 1
        else:
            h -= 1
            break
    return h
