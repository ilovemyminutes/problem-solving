'''문제: 소인수분해
소인수분해한 뒤 약수의 개수 구하기
- 소수를 먼저 찾고
    - 제곱근 기반으로 찾자
- 
'''
import sys
import time
from collections import defaultdict
import math

def is_prime(x):
    '''단일 정수의 소수 판단 활용'''
    if x in [2, 3]:
        return True
    for d in range(2, math.ceil(math.sqrt(x))+1):
        if x % d == 0:
            return False
    return True

def get_prime_list(n):
    '''n 이하 자연수 중 소수를 얻음'''
    arr = [False, False] + [True]*(n-1)
    primes = []
    for i in range(2, n+1):
        if arr[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = False
    return primes

def factorize(x): # x: 2보다 큰 자연수
    if is_prime(x):
        factorize_dict = {x:1}
        return factorize_dict
    prime_list = get_prime_list(x)
    factorize_dict = defaultdict(int)
    for p in prime_list:
        if x % p == 0:
            exp = 0
            while True:
                if x % p**(exp+1) != 0:
                    break
                exp += 1
            factorize_dict[p] = exp
    return factorize_dict

if __name__ == '__main__':
    line = int(sys.stdin.readline())
    factorized = factorize(line) # 소인수분해 결과
    num_divisors = 1 # 약수의 개수
    formula = '' # 출력할 수식

    for idx, (p, exp) in enumerate(sorted(factorized.items(), key=lambda x: x[0])):
        formula += f'{p}^{exp}'
        num_divisors *= (exp + 1)
        if idx != len(factorized) - 1:
            formula += ' * '

    print(formula.strip())
    print(num_divisors)
