'''좌표 정렬하기, https://www.acmicpc.net/problem/11650'''
import sys

FORMER, LATTER = 0, 1

n = int(input())

numbers = []
for _ in range(n):
    n1, n2 = sys.stdin.readline().split()
    numbers.append((int(n1), int(n2)))
    
numbers.sort(key=lambda x: x[LATTER])
numbers.sort(key=lambda x: x[FORMER])

for number in numbers:
    output = f'{number[FORMER]} {number[LATTER]}'
    sys.stdout.write(output + '\n')