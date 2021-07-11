'''https://www.acmicpc.net/problem/2644
문제:
    - 부모 자식 간 관계가 주어질 때, 주어진 두 사람의 촌수를 계산
'''
'''https://www.acmicpc.net/problem/2644
문제:
    - 가족관계도가 주어질 때, 주어진 두 사람 간 촌수를 계산
생각:
    - 트리순회문제 같은데, 이진트리는 아닌 트리 순회문제같음
'''
import sys
from collections import deque, defaultdict
input = sys.stdin.readline
        
n = int(input()) # 사람 수
t1, t2 = map(int, input().split())
m = int(input()) # 관계 수

# graph = [[0]*(n+1) for _ in range(n+1)]
graph = defaultdict(list)
visited = []

for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

que = deque([(t1, 0)])
while que:
    loc, num_links = que.popleft()
    if loc == t2:
        print(num_links)
        exit()
        break
    visited.append(loc)
    for nxt in graph[loc]:
        if nxt not in visited:
            que.append((nxt, num_links+1))
print(-1)