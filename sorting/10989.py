'''수 정렬하기 3, https://www.acmicpc.net/problem/10989'''
import sys
from collections import defaultdict
n = int(input())

num_dict = defaultdict(int)

for _ in range(n):
    new = int(sys.stdin.readline())
    num_dict[new] += 1

sorted_keys = sorted(list(num_dict.keys()))

for idx, num in enumerate(sorted_keys):
    output = f"{num}\n" * num_dict[num]
    print(output, end='')