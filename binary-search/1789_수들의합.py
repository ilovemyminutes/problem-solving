"""https://www.acmicpc.net/problem/1789
10
1 2 3 4
"""
s = int(input())

n = 0
current_sum = 0
num_to_add = 1
while current_sum <= s:
    current_sum += num_to_add
    num_to_add += 1
    n += 1

print(n-1)
    
    
    
