"""
연산 순서를 바꿔 최소값 만들기
0-9, +-으로 이루어짐
처음과 마지막 문자는 숫자
두 개 이상의 연산자 불가능

* 연산이 덧셈만 있다 -> 그냥 계산
* 뺄셈 연산이 적어도 하나 있다
    * 최대한 큰 수를 빼도록 하면 됨
    * - 뒤에 다시 -가 나올 때까지 괄호로 묶음
"""

formula = input()

if '-' in formula:
    formula = formula.split('-')
    output = 0
    for i, k in enumerate(formula):
        if i == 0:
            if '+' in k:
                k = sum(map(int, k.split('+')))
            else:
                k = int(k)
            output += k

        elif '+' in k:
            k = sum(map(int, k.split('+')))
            output -= k        
            
        else:
            output -= int(k)
            
elif '+' in formula:
    output = sum(map(int, formula.split('+')))
else:
    output = int(formula)

print(output)