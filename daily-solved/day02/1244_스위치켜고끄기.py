'''https://www.acmicpc.net/problem/1244
문제:
    - 스위치 켜짐(1) / 스위치 꺼짐(0)
    - 학생 각각에 1 이상 스위치 개수 이하인 자연수 하나씩 부여
    - 남학생:
        - 스위치 번호가 자기가 받은 수의 배수 => 스위치 상태 변경
            아니 스위치 번호가 뭐임
    - 여학생:
        - 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이면서
          가장 많은 스위치를 포함하는 구간을 찾아 해당 구간 내 스위치 상태 변경
          NOTE: 구간 내 스위치 수는 항상 홀수
          NOTE: 좌우대칭 := 구간 내 기준점 좌우 스위치 상태가 모두 같음
          
입력:
    - 스위치 개수 (int) <= 100
    - 스위치의 처음 상태
    - 각 학생의 성별과 받은 수
        - 남자 성별 1, 여자 성별 2
        - 0 < 학생이 받은 수 <= 스위치 개수
'''
MALE = 1
FEMALE = 2
ON = 1
OFF = 0

def get_available_indices(number: int, n: int) -> list:
    indices = []
    max_reach = min((n - number, number - 1))
    for m in range(max_reach+1):
        substatus = status[number-m:number+m+1]
        if substatus == substatus[::-1]: # 좌우대칭
            indices = [i for i in range(number-m, number+m+1)]
    return indices


n = int(input()) # 스위치 개수
status = [0] + list(map(int, input().split())) # 스위치 초기값
num_students = int(input()) # 학생 수

students = []
for _ in range(num_students):
    gender, number = map(int, input().split())
    students.append((gender, number))

for gender, number in students:
    if gender == MALE:
        max_multiples = n // number
        for m in range(1, max_multiples+1):
            status[m*number] = ON if status[m*number] == OFF else OFF
    else:
        indices = get_available_indices(number, n)
        if indices:
            for idx in indices:
                status[idx] = ON if status[idx] == OFF else OFF

output = []
suboutput = ''

num_print = 0
for s in status[1:]:
    suboutput += f'{str(s)} '
    num_print += 1
    if num_print % 20 == 0:
        output.append(suboutput.strip())
        num_print = 0
        suboutput = ''

if suboutput:
    output.append(suboutput.strip())

print('\n'.join(output))

