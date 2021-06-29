'''https://www.acmicpc.net/problem/1654
문제:
    - 길이가 모두 같은 N개의 랜선을 갖고 싶다
        - N개 이상의 랜선을 만드는 것도 허용
    - 이때, 랜선이 가질 수 있는 최대 길이?
입력:
    - K: 1 이상 1만 이하
    - N: 1 이상 1백만 이하
'''
import sys
from collections import Counter
input = sys.stdin.readline
k, n = map(int, input().split())
ropes = [int(input()) for _ in range(k)]

count_dict = Counter(ropes)
ropes = list(set(ropes))

max_length, min_length = max(ropes), 1

while min_length <= max_length:
    cut_length = (max_length + min_length) // 2
    num_cuts = sum(map(lambda x: (x // cut_length) * count_dict[x], ropes))
    if num_cuts >= n:
        min_length = cut_length + 1
    else:
        max_length = cut_length - 1

print(max_length)