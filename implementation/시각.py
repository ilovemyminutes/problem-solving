'''
모든 시각 중 3이 하나라도 포함되는 모든 경우의 수
'''
n = int(input()) # 00:00:00 ~ N:00:00

counts = 0
THREE = '3'

for H in range(n+1):
    for M in range(60):
        for S in range(60):
            t = f'{H:0>2d}{M:0>2d}{S:0>2d}'
            if THREE in t:
                counts += 1

print(counts)