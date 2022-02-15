"""
값을 인코딩하라는 의미인듯. 오름차순 인코딩
"""
import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().strip().split()))
encoder = {n: idx for idx, n in enumerate(sorted(set(sequence)))}

output = ""
for s in sequence:
    output += f"{encoder[s]} "
print(output.strip())
