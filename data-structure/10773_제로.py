"""
- K: [1, 1e+5)
"""
import sys

input = sys.stdin.readline

k = int(input())
numbers = [int(input()) for _ in range(k)]

refined = []
for n in numbers:
    if n == 0:
        refined.pop()
    else:
        refined.append(n)

print(sum(refined))