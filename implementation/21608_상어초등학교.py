"""문제 출처: https://www.acmicpc.net/problem/21608
교실 크기: NxN
    - 최좌상단 칸 (1, 1)
    - 최우하단 칸 (N, N)
학생 수: N^2 (1번부터 N^2번까지, 번호 중복 없음)

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

Goal: 학생의 만족도 총합 최대화
"""
n = int(input())
prefer_info = dict()
for _ in range(n**2):
    parsed = list(map(int, input().split()))
    student_id = parsed[0]
    preferences = parsed[1:]
    prefer_info [student_id] = preferences

print(prefer_info)


