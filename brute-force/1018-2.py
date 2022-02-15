"""
MxN 크기 보드
정사각형 색은 흑색 또는 흰색
8x8 체스판으로 만들자

- 잘라내는 위치는 어디나 가능
- 수정 횟수의 최솟값 구하기

- 불일치하는 갯수를 구하면 될듯?
"""
import sys
input = sys.stdin.readline

W = H = 8
CASE1 = [
    "WBWBWBWB",
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
    ]
CASE2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input().strip()) # WBWBBB...

# get patch
# (i, j): left-top start point
mismatches = 64
for i in range(n-H+1):
    for j in range(m-W+1):
        patch = [arr[i+k][j:j+8] for k in range(8)]

        # mismatch
        mismatches_case1 = 0
        mismatches_case2 = 0
        for r in range(H):
            p = patch[r]
            case1 = CASE1[r]
            case2 = CASE2[r]
            mismatches_case1 += sum([p[w] != case1[w] for w in range(W)])
            mismatches_case2 += sum([p[w] != case2[w] for w in range(W)])
            
        mis = min(mismatches_case1, mismatches_case2)
        if mis < mismatches:
            mismatches = mis

print(mismatches)


    




