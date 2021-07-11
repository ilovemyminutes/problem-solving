'''https://www.acmicpc.net/problem/4796
문제:
    - 캠핑장은 연속하는 p일 중 l일 동안만 사용
    - v일 짜리 휴가를 시작할 때, 최대 사용 가능한 캠핑장 일 수
'''
import sys
input = sys.stdin.readline
tests = []

while True:
    test = list(map(int, input().split())) # l, p, v
    if sum(map(lambda x: x==0, test)):
        break
    tests.append(test)


final_output = ''
for idx, (l, p, v) in enumerate(tests):
    max_num_camps = 0
    num_full_camps = v // p
    residue = v - num_full_camps * p
    num_residual_camps = min(residue, l)

    max_num_camps += l * num_full_camps
    max_num_camps += num_residual_camps
    
    output = f'Case {idx+1}: {max_num_camps}\n'
    final_output += output

print(final_output.strip())