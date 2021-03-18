"""https://www.acmicpc.net/problem/2798"""
import sys
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))

answer = None
diff = 1e6

for case in combinations(cards, 3):
    summation = sum(case)
    if summation > m:
        continue
    if abs(m - summation) <= diff:
        answer = summation
        diff = abs(m - summation)

print(answer)
