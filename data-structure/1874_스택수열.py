'''https://www.acmicpc.net/problem/1874
문제:
    - 1부터 n까지 수를 스택에 넣었다가 뽑아 늘어놓음
    - push: 오름차순 준수

목적: 임의 수열이 주어졌을 때, 스택으로 그 수열을 만들 수 있는지, 있다면 어떤 순서로 push, pop을 해줘야 하는지
생각:
    - 불능 체크를 어떻게 하지?
'''
n = int(input())
sequence = []
compare_sequence = []

for _ in range(n):
    sequence.append(int(input()))

signs = []
ongoing = []


cur_num = 1
origin_idx = 0
origin_seq_num = sequence[origin_idx]
while cur_num <= n:
    if cur_num <= origin_seq_num:
        ongoing.append(cur_num)
        signs.append('+')
        cur_num += 1
    else:
        compare_sequence.append(ongoing.pop())
        origin_idx += 1
        origin_seq_num = sequence[origin_idx]
        signs.append('-')        
        continue

while ongoing:
    signs.append('-')
    compare_sequence.append(ongoing.pop())

if compare_sequence == sequence:
    print('\n'.join(signs).strip())
else:
    print('NO')
