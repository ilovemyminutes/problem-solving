'''https://www.acmicpc.net/problem/14888
문제:
    - N개의 수로 이루어진 수열
    - N-1개의 연산자
        - 연산자: 가감승제
    - 식의 결과가 최대, 최소인 경우 각각을 출력

입력:
    - N: 2 이상 11 이하
        => permutation 사용하면될듯
'''
from itertools import permutations
n = int(input())
sequence = list(map(int, input().split()))
num_adds, num_subs, num_muls, num_divs = map(int, input().split()) # 총 n-1개
operations = ['+']*num_adds + ['-']*num_subs + ['*']*num_muls + [r'/']*num_divs

cases = set(permutations(operations, r=n-1))

min_output = int(1e+9)
max_output = -int(1e+9)

for case in cases:
    output = sequence[0]
    for idx, oper in enumerate(case):

        if oper == '-':
            output -= sequence[idx+1]

        elif oper == '+':
            output += sequence[idx+1]

        elif oper == r'/':
            if output < 0:
                output = -1 * (abs(output) // sequence[idx+1])
            else:
                output = output // sequence[idx+1]

        elif oper == '*':
            output *= sequence[idx+1]

    if output < min_output:
        min_output = output
    if output > max_output:
        max_output = output

print(max_output)
print(min_output)




