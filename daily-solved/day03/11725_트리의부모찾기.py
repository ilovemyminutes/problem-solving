'''https://www.acmicpc.net/problem/11725

문제: 루트 없는 트리가 주어지고, 1이 부모 노드라고 할 때, 나머지 노드별 부모 노드 찾기
생각:
    - DFS로 불편 되것다리
'''
n = int(input()) # 노드 수
tree = {i: [] for i in range(1, n+1)}
visited = [False for i in range(n+1)]

for _ in range(n-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

parent_for_each_idx = [None for _ in range(n+1)] # 2번~N번

parent = 1
stack = [(parent, node) for node in tree[parent]]
visited[parent] = True

while stack:
    parent, node = stack.pop()
    parent_for_each_idx[node] = str(parent)
    visited[node] = True

    linked = [n for n in tree[node] if visited[n] is not True]
    for l in linked:
        stack.append((node, l))

print('\n'.join(parent_for_each_idx[2:]))


