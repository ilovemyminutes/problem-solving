'''https://www.acmicpc.net/problem/9012
괄호문자열, PS: 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열
VPS: 괄호 모양이 올바르게 구성된 문자열
    - '()': 올바른 구성
    - 'x'가 올바른 구성이면 '(x)'도 올바른 구성
    - 'x', 'y'가 올바른 구성이면 'xy'도 올바른 구성

목적: VPS 검증
입력:
    - 테스트 케이스 수 T
    - T개 테스트 괄호문자열 - 길이 50 이하
출력:
    - VPS일 경우 'YES', 아닐 경우 'NO'

생각:
    - 루프 도는걸 상상
    - 좌괄호 수보다 우괄호 수가 많으면 안되겠지
    - 첫문자열은 우괄호일 수 없음
'''

t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(input())

for brack_str in test_cases:
    num_left_brackets = 0
    num_right_brackets = 0
    is_vps = True
    for b in brack_str:
        if b == '(':
            num_left_brackets += 1
        else:
            num_right_brackets += 1
        if num_left_brackets < num_right_brackets:
            is_vps = False
            break

    if num_left_brackets != num_right_brackets:
        is_vps = False
    if is_vps:
        print('YES')
    else:
        print('NO')
    
    

        
        
    


