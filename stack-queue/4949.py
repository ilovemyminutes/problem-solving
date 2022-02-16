"""괄호 균형
균형잡혀져있음의 정의
- 소/대괄호는 소/대괄호랑
- 괄호는 짝이 맞게 주어짐

문자열이 주어졌을 때 균형이 맞춰져 있는지 여부
"""
import sys
input = sys.stdin.readline

output = ''
while True:
    string = input().rstrip()
    if string == '.':
        break
    
    pre_c = ''
    worthy = True
    l_ro, r_ro = 0, 0
    l_sq, r_sq = 0, 0
    for cur_c in string:

        if cur_c not in ['(', ')', '[', ']']:
            continue
        elif cur_c == '(':
            l_ro += 1
        elif cur_c == ')':
            if pre_c != '(':
                print('pre_c', pre_c)
                worthy = False
                break
            r_ro += 1
        elif cur_c == '[':
            l_sq += 1
        elif cur_c == ']':
            if pre_c != '[':
                print('pre_c', pre_c)
                worthy = False
                break

        pre_c = cur_c
        if l_ro == 1 and r_ro == 1:
            l_ro, r_ro = 0, 0
        if l_sq == 1 and r_sq == 1:
            l_sq, r_sq = 0, 0

    if worthy and (l_ro == r_ro) and (l_sq == r_sq):
        output += 'yes\n'
    else:
        output += 'no\n'

print(output.rstrip())




