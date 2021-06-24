'''https://www.acmicpc.net/problem/1874
문제:
    - 1부터 n까지 수를 스택에 넣었다가 뽑아 늘어놓음
    - push: 오름차순 준수
목적: 임의 수열이 주어졌을 때, 스택으로 그 수열을 만들 수 있는지, 있다면 어떤 순서로 push, pop을 해줘야 하는지
생각:
    - 기준 수열의 가장 앞의 값을 우선 기준 삼음. 이걸 K(0)이라고 하자
    - 1부터 시퀀싱하는데, K(0)보다 작거나 같은 값이 나오는 동안에는 push
        - 기준 수열에 맞게 값을 내뱉어야 되니까, 그 값에 다다를 때까지 push를 하는 것
    - 시퀀싱한 값이 기준값(K(0))보다 크면, pop
        - 기준 수열에 맞는 값을 pop하게 되는것!
        - pop을 했는데 기준 수열에 맞지 않는 값이 나왔다 => 불능
        - pop을 함으로써 기준 수열의 값에 대응되는 값은 시퀀싱이 된 것이니, 이제 기준값을 바꿈. 즉, 기준 값이 K(1)이 됨
    - N까지 시퀀싱할 때까지 반복
    - 반복이 끝났을 때, 지금까지 활용한 스택이 여전히 차있으면, 모조리 pop을함으로써 나머지 수열을 메꿈
    - 시퀀싱을 통해 얻은 수열과 기준 수열을 비교한 뒤, 같으면 부호 수열을 출력하고, 같지 않으면 'NO'를 출력
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
