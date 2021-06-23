'''https://www.acmicpc.net/problem/2504
올바른 괄호열의 조건
    한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다. 
    만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
    X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.

올바른 괄호열일 때 값.(X, Y: 올바른 괄호열)
    value(‘()’) = 2
    value(‘[]’) = 3 
    value('(X)') = 2 * value('X')
    value('[X]') = 3 * value('X')
    value('XY') = value('X') + value('Y')

올바르지 않은 괄호열일 때의 괄호값: 0

입력: 길이 1~30 괄호열
출력: 괄호열의 값
'''
sequence = input()
stack = []

for c in sequence:
    if c == '(' or c == '[':
        stack.append(c)

    elif c == ')' and stack:
        temp = 0 # 점수를 누적할 임시 변수
        value = 0 # 최종 점수
        while stack:
            popped = stack.pop()

            # 점수일 경우
            if isinstance(popped, int):
                temp += popped
                continue

            # 올바르지 않은 괄호
            elif popped != '(':
                print(0)
                exit()
            
            # 올바른 괄호
            else:
                value = 2 * temp if temp > 0 else 2
                stack.append(value)
                break

    elif c == ']' and stack:
        temp = 0 # 점수를 누적할 임시 변수
        value = 0 # 최종 점수
        while stack:
            popped = stack.pop()

            # 점수일 경우
            if isinstance(popped, int):
                temp += popped
                continue

            # 올바르지 않은 괄호
            elif popped != '[':
                print(0)
                exit()
            
            # 올바른 괄호
            else:
                value = 3 * temp if temp > 0 else 3
                stack.append(value)
                break
    else:
        break


if sum(map(lambda x: isinstance(x, int), stack)) == len(stack):
    print(sum(stack))
else:
    print(0)
            
            

        
    

