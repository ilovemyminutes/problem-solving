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

for test in tests:
    num_members = 0
    test.sort(key=lambda x: x[0])
    for idx in range(len(test)):
        if idx == 0:
            max_interview_rank = test[idx][1]
            num_members += 1
        elif max_interview_rank > test[idx][1]:
            max_interview_rank = test[idx][1]
            num_members += 1        
    print(num_members)


