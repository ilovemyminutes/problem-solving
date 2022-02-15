"""
n: 1~10
target(k): 1~1억
각 value: 1~1백만
  * 각 동전은 무한개씩 존재함을 가정
- a1 = 1
- n >= 2일 때, a_{n}은 a_{n-1}의 배수임

target을 만드는 데 필요한 동전 수의 최솟값 구하기
"""
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coins = []
for _ in range(n):
    v = int(input())  # value
    if v == k:
        print(1)
        exit()
    elif v < k:
        coins.append(v)
coins = coins[::-1]  # descending sort

min_coins = int(1e+8)
for start_idx in range(len(coins)):
    cur_value = 0
    res_value = k
    cur_coins = 0

    for i in range(start_idx, len(coins)):
        v = coins[i]
        q = res_value // v
        vq = v*q

        cur_value += vq
        res_value -= vq
        cur_coins += q

        if cur_value == k and cur_coins < min_coins:
            min_coins = cur_coins 
            break

print(min_coins)