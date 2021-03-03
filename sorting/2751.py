'''수 정렬하기 2, https://www.acmicpc.net/problem/2751'''
import sys

n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for number in numbers:
    sys.stdout.write(str(number) + '\n')
