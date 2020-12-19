"""https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
트럭: 1초에 1만큼 이동
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    timeline = [0 for i in range(len(truck_weights) * bridge_length + 1)]
    truck_weights = deque([(idx, t) for idx, t in enumerate(truck_weights)])
    start = 0
    end = start + bridge_length
    while len(truck_weights) > 0:
        truck = truck_weights.popleft()
        if truck[0] == 0:  # 첫째 트럭
            timeline[start:end] = list(
                map(lambda x: x + truck[-1], timeline[start:end])
            )
        else:
            start += 1
            while timeline[start] + truck[-1] > weight:
                start += 1
            end = start + bridge_length
            timeline[start:end] = list(
                map(lambda x: x + truck[-1], timeline[start:end])
            )
    total_time = timeline.index(0) + 1
    return total_time
