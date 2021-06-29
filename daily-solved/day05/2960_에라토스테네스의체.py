'''https://www.acmicpc.net/problem/2960
에라토스테네스의 체
    - 2부터 N까지 모든 정수를 적는다.
    - 아직 지우지 않은 수 중 가장 작은 소수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
    - P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
    - 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
'''
import math
def is_prime(p):
    '''2 이상의 자연수 입력을 가정'''
    if p <= 3:
        return True
    else:
        root = math.ceil(math.sqrt(p))
        for r in range(2, root+1):
            if p % r == 0:
                return False
        return True

n, k = map(int, input().split())
numbers = [i for i in range(n+1)]
removed = [False for _ in range(n+1)]

num = 2
while not all(removed):
    if removed[num] is False:
        if is_prime(num):
            multiples = [num*m for m in range(1, (n//num)+1) if removed[num*m] is False]
            for m in multiples:
                removed[m] = True
                k -= 1
                if k == 0:
                    print(m)
                    exit()
    else:
        num += 1
                
                

