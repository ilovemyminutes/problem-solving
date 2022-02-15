"""N개 회의에 대한 사용표 만들기
- 각 회의 I: 시작과 끝 인터벌 주어짐
- 겹치지 않게 회의할 수 있는 회의 최대 수

"""
import sys
input = sys.stdin.readline

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)] # {start: interval}
intervals.sort(key=lambda x: (x[1], x[0]))

num_classes = 0
end = 0

for cur_s, cur_e in intervals:
    if cur_s >= end:
        end = cur_e
        num_classes += 1

print(num_classes)