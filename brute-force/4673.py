"""
셀프넘버 

- d(n): 자연수 n에 대해 n과 n의 각 자리수의 합
    - d(d(....d(n)))의 형태로 무한 수열을 만들 수 있음
    - n: 생성자
    - 셀프넘버: 생성자가 없는 숫자 (span할 수 없는 숫자)
"""

def d(num: int) -> int:
    output = num
    for n in str(num):
        output += int(n)
    return output

gen_table = {i:False for i in range(1, 10001)}

for gen in range(1, 10001):
    if gen_table[gen]:
        continue
    
    while True:
        gen = d(gen)
        if gen > 10000:
            break
        gen_table[gen] = True

answer = ''
for num in range(1, 10001):
    if not gen_table[num]:
        answer += f"{num}\n"

print(answer.rstrip())
        

