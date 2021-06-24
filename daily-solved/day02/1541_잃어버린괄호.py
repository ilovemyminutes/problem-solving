'''https://www.acmicpc.net/problem/1541
식 구성: 양수, +, -, (소)괄호

목적: 괄호를 활용해 식의 값을 최소로 만들기
입력: 양수, +, -로 구성된 수식
    - 연속해서 두 개 이상의 연산자가 나타나지 않음
    - 5자리보다 많이 연속되는 숫자는 없음
    - 가장 처음과 마지막 문자는 숫자임
    - 양수는 다섯자리 이하
    - 수식 길이 <= 50

생각:
    - 최소로 만든다는 걸 규칙을 어떻게 정하지?
    - 괄호의 수에는 제한이 없고
        - 괄호를 삽입하는 상상보다는 연산 순서를 뒤바꾼다고 생각해야겠다
    - 음수 뒤의 숫자를 최대한 더해주는게 좋을 것 같다
    55 - 50 + 40 -> 55 - (50 + 40)
    확장: 55 - 50 + 40 - 30 + 20 + 40 -> 55 - (50 + 40) - (30 + 20 + 40) = 55 - 90 - 90 = -125
        - 그럼 수식을 리스트로 파싱한 뒤에, 덧셈 연산자를 다 제외하고, - 를 분기점으로 그룹화, 각각 summation한 것을 모두 더하면 되지 않을까?

'''
raw = input()

expression = []
integer_frame = ''
for k in raw:
    if k.isnumeric():
        integer_frame += k
    elif k == '-':
        expression.append(int(integer_frame))
        expression.append(k)
        integer_frame = ''
    else:
        expression.append(int(integer_frame))
        integer_frame = ''
if integer_frame:
    expression.append(int(integer_frame))



# 뺄셈이 한번도 없을 경우
if '-' not in expression:
    answer = sum(expression)
else:
    answer = 0
    subtotal = 0
    sign = +1

    for idx, e in enumerate(expression):
        if isinstance(e, int):
            subtotal += e
            if idx == len(expression) - 1:
                answer -= subtotal
        else:
            answer += sign * subtotal
            sign = -1 if sign == +1 else sign
            subtotal = 0
        
print(answer)

    