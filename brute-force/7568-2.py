"""
- 덩치: 키와 몸무게 모두 크면 덩치가 더 크다
- 덩치 등수: 목록 내 자신보다 덩치가 큰 사람의 수
"""
import sys
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    w, h = map(int, input().split())
    info.append((w, h))

result = ''
for idx, (cur_w, cur_h) in enumerate(info):
    if idx == 0:
        compare = info[idx+1:]
    elif idx == n - 1:
        compare = info[:idx]
    else:
        compare = info[:idx] + info[idx+1:]

    rank = 1
    for (comp_w, comp_h) in compare:
        if comp_w > cur_w and comp_h > cur_h:
            rank += 1
    result += f'{rank} '

print(result.strip())