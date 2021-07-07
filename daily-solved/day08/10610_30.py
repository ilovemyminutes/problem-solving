'''https://www.acmicpc.net/problem/10610
문제:
    - 주어진 자연수를 재배열하여 30의 배수가 되는 가장 큰 수 만들기
        - 1 이상 10만 이하
    - 존재하지 않을 경우 -1을 출력
해결:
    - 30의 배수일 조건 <=> 2의 배수 & 3의 배수 & 5의 배수
    - 2의 배수 & 5의 배수: 끝자리가 반드시 0
    - 3의 배수: 모든 수를 더했을 때 3의 배수
    - 30의 배수가 될 경우 하나의 0을 맨 뒤로 뺀 뒤 가장 큰 수 찾으면 
        - 내림차순 정렬
        - 가장 마지막 원소가 0인지 확인
        - 모든 값을 더했을 때 3의 배수인지 확인
'''
number = list(map(int, list(input())))
number.sort(reverse=True)

if number[-1] == 0 and sum(number) % 3 == 0:
    output = ''.join(list(map(str, number)))
else:
    output = -1

print(output)