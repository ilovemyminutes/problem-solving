'''좌표 정렬하기 2, https://www.acmicpc.net/problem/11651'''

import sys

FORMER, LATTER = 0, 1

n = int(input())

numbers = []
for _ in range(n):
    n1, n2 = sys.stdin.readline().split()
    numbers.append((int(n1), int(n2)))

numbers.sort(key=lambda x: x[FORMER])
numbers.sort(key=lambda x: x[LATTER])

for number in numbers:
    output = f'{number[FORMER]} {number[LATTER]}'
    sys.stdout.write(output + '\n')