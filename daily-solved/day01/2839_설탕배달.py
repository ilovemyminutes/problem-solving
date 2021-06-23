'''https://www.acmicpc.net/problem/2839
5킬로 봉지, 3킬로 봉지
봉지를 최소한으로 들고갈 경우, 봉지 개수 구하기
'''
import math 
n = int(input())

max_b5 = math.floor(n // 5)
num_b5_cand_list = sorted([i for i in range(0, max_b5+1)], reverse=True)
num_b3 = 0

for num_b5 in num_b5_cand_list:
    residue = n  - (num_b5 * 5)
    if residue % 3 == 0:
        num_b3 = residue // 3
        break
        
answer = num_b5 + num_b3
print(answer)
