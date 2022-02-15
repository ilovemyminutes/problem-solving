"""https://www.acmicpc.net/problem/18870
문제:
    - 수직선 위 N개 좌표
    - X_i'(X_i 압축 결과) > |{X_j | X_i > X_j}|
입력:
    - 첫째줄: N
    - 둘째줄: X1, ..., XN
출력:
    - 압축값의 시퀀스
"""
n = int(input())
sequence = list(map(int, input().split()))
ordered = sorted(list(set(sequence)))  # 오름차순 정렬
order_dict = {s: idx for idx, s in enumerate(ordered)}
length = len(ordered)

output = ""
for s in sequence:
    value = order_dict[s]
    output += f"{value} "

print(output.strip())
