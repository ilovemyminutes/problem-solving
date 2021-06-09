"""https://www.acmicpc.net/problem/2417"""
from math import sqrt, floor
n = int(input())
root_n = floor(sqrt(n))
q = root_n

while q**2 < n:
    q += 1

print(q)