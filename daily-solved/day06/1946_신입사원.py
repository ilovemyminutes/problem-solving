'''https://www.acmicpc.net/problem/1946
문제:
    - 서류 성적, 면접 성적 중 적어도 하나가 다른 지원자보다 높아야 함
'''
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    test = [tuple(map(int, input().split())) for _ in range(n)] # (서류, 면접)
    tests.append(test)
    




