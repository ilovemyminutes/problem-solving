# Tree

## Definition

- 트리 구조: 1개 이상의 유한한 개수의 노드(node=vertex) 집합
- 루트 노드와 0개 이상의 겹치지 않는 하위 나무 구조의 집합
- 트리 구성
  - 노드
  - 엣지
  - 경로: 엣지에 의해 연결된 노드의 집합
  - 루트 노드: 최상위 노드
  - 부모 노드: 기준 노드의 직계 상위 노드
  - 자식 노드: 기준 노드의 직계 하위 노드
  - 형제 노드: 기준 노드와 같은 부모 노드를 지닌 노드
  - 리프, 잎: 자식이 없는 노드
  - 서브 트리: 큰 트리에 포함된 작은 트리
  - 차수(degree): 하위 서브 트리 개수
  - 레벨: 루트 노드부터 최하위 노드까지 중첩되지 않은 경로의 노드 수
  - 크기(size): 트리 내 모든 노드 수
  - *트리 크기가 N일 때 간선 개수는 N-1
- 이진 트리
  - 모든 내부 노드가 둘 이하의 자식 노드를 가진 트리
  - 루트 노드를 기준으로 왼쪽 이진트리, 오른쪽 이진트리로 구성된 집합
- 완전 이진 트리
  - 가장 마지막 레벨을 제외한 모든 노드들이 꽉 차있고(자식 노드 수=2) 마지막 레벨은 왼쪽부터 오른쪽 끝 노드까지 빈칸이 없는 트리
- 포화 이진 트리
  - 마지막 레벨까지 완전히 꽉차있는 트리
- 이진 트리의 순회
  - 전위 순회(preorder traverse): 루트를 먼저 방문 - 루트 > 왼쪽 자식 > 오른쪽 자식
  - 중위 순회(inorder traverse): 왼쪽 하위 트리 방문 후 루트 노드 방문 - 왼쪽 자식 > 루트 > 오른쪽 자식
  - 후위 순회(postorder traverse): 하위 트리를 모두 방문하고 루트 노드 방문 - 왼쪽 자식 > 오른쪽 자식 > 루트
  - 층별 순회(level order traverse): 위쪽 노드부터 아래방향으로 차례대로 방문 - 

## Implementation

```python
class Node: # 루트 노드(현 시점), 그에 대한 왼쪽/오른쪽 자식노드에 대한 인스턴스를 받음
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회, preorder traversal
def pre_order(node):
    '''우선순위: 루트 -> 왼쪽자식 -> 오른쪽 자식'''
    print(node.data, end=' ') # 자기 자신(루트)을 출력 왼쪽자식, 오른쪽자식 순회
    if node.left_node is not None:
        pre_order(tree[node.left_node])
    if node.right_node is not None:
        pre_order(tree[node.right_node])

# 중위 순회, inorder traversal
def in_order(node):
    '''우선순위: 왼쪽자식 -> 루트 -> 오른쪽 자식
    재귀를 활용함으로써 가장 마지막 왼쪽 자식부터 짚어보는 것!
    '''
    if node.left_node is not None:
        in_order(tree[node.left_node])
    print(node.data, end=' ') # 왼쪽 자식을 출력하고 루트를 출력, 이후 오른쪽 자식 순회
    if node.right_node is not None:
        in_order(tree[node.right_node])

# 후위 순회, post order traversal
def post_order(node):
    '''우선순위: 왼쪽자식 -> 오른쪽 자식 -> 루트
    재귀를 활용함으로써 가장 마지막 왼쪽 자식부터 짚어보는 것!
    '''
    if node.left_node is not None:
        post_order(tree[node.left_node])
    if node.right_node is not None:
        post_order(tree[node.right_node])
    print(node.data, end=' ') # 왼쪽자식과 오른쪽자식을 출력, 이후 루트 노드를 순회


# 트리 구조 구현 - 딕셔너리 활용하자!
n = int(input()) # 노드 수
tree = dict()

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

# pre-order traversal
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
```