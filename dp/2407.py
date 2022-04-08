"""조합
바텀업 가능할듯
"""
n, m = map(int, input().split())

perm1 = [i for i in range(max([n-m, m])+1, n + 1)]
perm2 = [i for i in range(1, min([n-m, m]) + 1)]


denom, divisor = 1, 1
for p in perm1:
    denom *= p
for p in perm2:
    divisor *= p

print(denom // divisor)