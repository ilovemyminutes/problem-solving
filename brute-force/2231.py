"""https://www.acmicpc.net/problem/2231
분해합: N + (N을 이루는 각 자리수의 합)
생성자: 어떤 자연수 M의 분해합이 N => 생성자=M
생성자가 없는 경우 0 출력
"""


def decompose_sum(number: int) -> int:
    parsed_sum = sum(map(int, list(str(number))))
    return number + parsed_sum


n = int(input())

for i in range(1, n):
    if decompose_sum(i) == n:
        print(i)
        exit()

print(0)
