"""https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
초당 최대 처리량: 임의 시간부터 1초  간 처리하는 요청의 최대 개수
lines: N개의 로그 문자열로 구성
응답완료시간 S: 고정 길이 형식 '2016-09-15 hh:mm:ss.sss'
처리시간 T: 0.312s. 소수점 셋째 자리까지 기록. 시작시간과 끝시간을 포함
0.001<=T<=3.000

마이크로 초: 10e-6 초
"""
from datetime import datetime, timedelta


def solution(lines):
    intervals = list(map(lambda x: _moment_to_interval(x), lines))
    moments = get_moments(lines)
    counts = [0 for i in range(len(moments))]
    for idx in range(len(moments)):
        for interval in intervals:
            if isin(moments[idx], interval[0], interval[-1]):
                # print(moments[idx])
                # print(interval)``
                # print()
                counts[idx] += 1
    return max(counts)


def get_moments(test: "처음 입력 받은 리스트"):
    moments = set()
    for moment in test:
        end = datetime.strptime(moment.split(" ")[1], "%H:%M:%S.%f")  # 응답완료시간
        interval = float(moment.split(" ")[-1][:-1])  # 처리시간(sec)
        start = end - timedelta(seconds=interval)
        moments.add(end)
        moments.add(start)
    return sorted(list(moments))


def _moment_to_interval(moment):
    end = datetime.strptime(moment.split(" ")[1], "%H:%M:%S.%f")  # 응답완료시간
    interval = float(moment.split(" ")[-1][:-1]) - 0.001  # 처리시간(sec)
    start = end - timedelta(seconds=interval)
    return (start, end)


def isin(left, start: "샘플의 시작점", end: "샘플의 끝점") -> bool:
    right = left + timedelta(seconds=0.999)
    return False if end < left or right < start else True
