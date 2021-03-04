"""통계학, https://www.acmicpc.net/problem/2108"""
import sys
from collections import Counter
import heapq


def get_avg(sorted_data: list) -> int:
    output = round(sum(sorted_data) / len(sorted_data))
    return output


def get_median(sorted_data: list) -> int:
    if len(sorted_data) % 2 == 0:
        latter = len(sorted_data) // 2
        former = latter - 1
        median = round((sorted_data[former] + sorted_data[latter]) / 2)
    else:
        mid = len(sorted_data) // 2
        median = sorted_data[mid]
    return median


def get_interval(sorted_data: list) -> int:
    maximum = sorted_data[-1]
    minimum = sorted_data[0]
    return maximum - minimum


def get_mode(data: list) -> int:
    FREQ, NUM = 0, 1
    counts = [(-freq, num) for num, freq in Counter(data).items()]

    if len(counts) == 1:
        mode = counts[0][NUM]
        return mode

    mode_list = []
    for _ in range(2):
        heapq.heapify(counts)
        mode_list.append(counts.pop(0))
    if mode_list[0][FREQ] != mode_list[1][FREQ]:
        mode = mode_list[0][NUM]
    else:
        mode = mode_list[1][NUM]
    return mode


n = int(input())
numbers = sorted([int(sys.stdin.readline()) for _ in range(n)])

print(get_avg(numbers))
print(get_median(numbers))
print(get_mode(numbers))
print(get_interval(numbers))
