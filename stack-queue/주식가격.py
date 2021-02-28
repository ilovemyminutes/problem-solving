"""https://programmers.co.kr/learn/courses/30/lessons/42584"""

from collections import deque


def solution(prices):
    prices = deque(prices)
    result = list()

    while True:
        state = prices.popleft()
        if len(prices) == 0:
            result.append(0)
            break
        combo = 0
        for price in prices:
            combo += 1
            if state <= price:
                pass
            else:
                break
        result.append(combo)

    return result
