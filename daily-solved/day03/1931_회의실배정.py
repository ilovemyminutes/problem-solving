'''https://www.acmicpc.net/problem/1931
문제: 회의 시간과 회의 일정이 주어질 때, 하나의 강의실에서 할 수 있는 최대 회의 수 구하기

생각:
    - 시작점을 기준으로 정렬 진행
    - 다음의 우선순위를 바탕으로 회의 일정을 제거
        - 겹치는 스케줄이 가장 많은 회의 제거
            - 겹치는 스케줄 수가 가장 많은 회의 수가 2개 이상일 경우 긴 회의를 제거
        - 겹치는 스케줄이 없을 때까지 반복
        - '겹친다' := (s1, e1), (s2, e2)에 대하여(s1 <= s2) e1 > s2인 경우
'''
n = int(input())
intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))

# 끝나는 시간을 기준으로 오름차순 정리 후 시작 시간을 기준으로 오름차순 정리
    # 일찍 끝나는 회의 순으로 정렬되고, 같은 시각에 끝날 경우 더 일찍 시작하는 회의가 앞섬
    # 반복문을 돌면서, 가장 일찍 끝나는 회의부터 체크
    # 이후 오버랩이 발생하는 회의는 패스
intervals.sort(key=lambda x: (x[1], x[0]))
num_classes = 0
start = 0

for nxt_start, nxt_end in intervals:
    if nxt_start >= start:
        start = nxt_end
        num_classes += 1

print(num_classes)
