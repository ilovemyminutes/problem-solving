'''https://www.acmicpc.net/problem/7568
A: (x, y), B: (p, q)
A의 덩치가 크다: x > p and y > q
덩치 등수: 자신보다 더 큰 덩치의 사람 수
'''
import sys

def is_bigger(p1: tuple, p2: tuple) -> bool:
    '''
    p1의 덩치가 p2보다 큰 경우 True, 비교가 불가하거나 크지 않은 경우 False
    '''
    WEIGHT, HEIGHT = 0, 1
    return True if (p1[WEIGHT] > p2[WEIGHT]) and (p1[HEIGHT] > p2[HEIGHT]) else False
    
n = int(input())
profiles = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    profiles.append((weight, height))

ranks = []

for p1 in profiles:
    rank = 1
    for p2 in profiles:
        if is_bigger(p2, p1):
            rank += 1
    ranks.append(str(rank))

print(' '.join(ranks))

