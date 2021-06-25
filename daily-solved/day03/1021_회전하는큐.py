'''https://www.acmicpc.net/problem/1021'''
from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

num_operations = 0
sequence = deque([i for i in range(1, n+1)])
for t in targets:
    if sequence[0] == t:
        sequence.popleft()
    else:
        target_idx = sequence.index(t)
        if len(sequence) - target_idx >= target_idx:
            num_operations += target_idx
            sequence = deque(list(sequence)[target_idx:] + list(sequence)[:target_idx])
            sequence.popleft()
        else:
            num_operations += len(sequence) - target_idx
            sequence = deque(list(sequence)[target_idx:] + list(sequence)[:target_idx])
            sequence.popleft()

print(num_operations)
    