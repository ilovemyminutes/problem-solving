'''https://programmers.co.kr/learn/courses/30/lessons/42578'''
from collections import Counter
from itertools import combinations
from functools import reduce
import operator as op

def solution(clothes):
    counts = tuple(Counter(map(lambda x: (x[-1]), clothes)).values())
    n_class = len(counts)
    if sum(tuple(map(lambda x: x==1, counts))) == n_class:
        return sum([nCr(n_class, i) for i in range(1, n_class+1)])
    else:
        result = 0
        for n in range(1, n_class+1):
            temp = list(combinations(counts, n))
            result += sum(list(map(vec_mul, temp)))
        return result

def vec_mul(x:tuple) -> int:
    if len(x) == 1:
        return x[0]
    else:
        return reduce(op.mul, x)

def nCr(n:int, r:int):
    numer = reduce(op.mul, range(n-r+1, n+1))
    denom = reduce(op.mul, range(1, r+1))
    return int(numer / denom)