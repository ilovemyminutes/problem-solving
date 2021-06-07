"""https://www.acmicpc.net/problem/9012
여는 괄호 나오면 닫는 괄호 나와야함
"""

t = int(input())
result = ''

def is_vps(test: str):

    # 초벌 필터링
    if test[0] == ')' or test[-1] == '(':
        return 'NO'

    # 좌우 괄호 총 등장 횟수
    num_lefts = 0
    num_rights = 0

    # 완전한 쌍이 되기 전까지 좌우 괄호 등장 횟수
    l_stacks = 0
    r_stacks = 0
    cur_type = '(' # 시작 괄호

    for char in test:

        # 좌괄호 등장
        if char == '(':
            num_lefts += 1
            if cur_type == char: # 이전 괄호와 일치할 경우
                l_stacks += 1
            else: # 이전 괄호와 불일치할 경우
                l_stacks += 1
                cur_type = char
        else:
            num_rights += 1
            if cur_type == char: # 이전 괄호와 일치할 경우
                r_stacks += 1
            else: # 이전 괄호와 불일치할 경우
                r_stacks += 1
                cur_type = char

        # 완전한 쌍이 구성될 경우 l_stacks, r_stack 각각 초기화
        if l_stacks == r_stacks: 
            l_stacks = 0
            r_stacks = 0
            cur_type = '('

        # 우괄호 등장 횟수 더 많이 등장할 경우 완전한 쌍이 구성될 수 없음
        elif l_stacks < r_stacks:
            return 'NO'
    
    # 좌우 괄호 총 등장 횟수가 불일치하면 VPS가 아님
    if num_lefts != num_rights:
        return 'NO'
    else:
        return 'YES'


for _ in range(t):
    test = input()
    vps = f"{is_vps(test)}\n"
    result += vps

print(result)
