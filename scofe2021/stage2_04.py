'''
색인: 알파벳 소문자로 구성
'''
n = int(input())
s_list = []
for _ in range(n):
    s = input()
    if len(s) >= 2:
        s_list.append(s)
q = int(input())
q_list = [input() for _ in range(q)]

for q in q_list:
    output = [q in x for x in s_list]
    print(sum(output))