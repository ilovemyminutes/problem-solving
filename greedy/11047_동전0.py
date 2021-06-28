'''https://www.acmicpc.net/problem/11047
문제:
    - 가진 동전 종류는 N가지. 각 동전을 무한개로 가지고 있음을 가정
    - 최소한의 동전만을 활용해 K의 값어치를 만들 때, 해당 최소값을 구하시오

생각:
    - K보다 작거나 같은 동전 중 가장 큰 동전부터 카운팅하면 되겠다
    - 오름차순으로 코인 종류가 입력되니, 스택 구조의 pop을 이용하면 될듯
'''
import sys
input = sys.stdin.readline

# initailize
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# solve
value = 0
num_total_used = 0
while value != k:
    coin = coins.pop()
    if coin <= k - value:
        num_used = (k - value) // coin
        num_total_used += num_used
        value += num_used * coin
        
print(num_total_used)
        