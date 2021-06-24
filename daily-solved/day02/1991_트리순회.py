'''https://www.acmicpc.net/problem/1991'''

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

n = int(input()) # 노드 수
tree = dict()

for _ in range(n):
    data, left_node, right_node = input().split()
    left_node = None if left_node == '.' else left_node
    right_node = None if right_node == '.' else right_node
    node = Node(data, left_node, right_node)
    tree[data] = node

def pre_order(node: Node):
    '''전위순회 - 루트 -> 왼쪽 자식 -> 오른쪽 자식'''
    print(node.data, end='')
    if node.left_node is not None:
        pre_order(tree[node.left_node])
    if node.right_node is not None:
        pre_order(tree[node.right_node])

def in_order(node: Node):
    '''중위순회 - 왼쪽 자식 -> 루트 -> 오른쪽 자식'''
    if node.left_node is not None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node is not None:
        in_order(tree[node.right_node])

def post_order(node: Node):
    '''중위순회 - 오른쪽 자식 -> 왼쪽 자식 -> 루트'''
    if node.left_node is not None:
        post_order(tree[node.left_node])
    
    if node.right_node is not None:
        post_order(tree[node.right_node])
    print(node.data, end='')

# def pre_order(node: Node, result=''):
#     '''전위순회 - 루트 -> 왼쪽 자식 -> 오른쪽 자식'''
#     result += node.data
#     if node.left_node is not None:
#         result = pre_order(tree[node.left_node], result)
#     if node.right_node is not None:
#         result = pre_order(tree[node.right_node], result)
#     return result

# def in_order(node: Node, result=''):
#     '''중위순회 - 왼쪽 자식 -> 루트 -> 오른쪽 자식'''
#     if node.left_node is not None:
#         result = in_order(tree[node.left_node])
#     result += node.data
#     if node.right_node is not None:
#         result = in_order(tree[node.right_node])
#     return result

# def post_order(node: Node, result=''):
#     '''중위순회 - 오른쪽 자식 -> 왼쪽 자식 -> 루트'''
#     if node.left_node is not None:
#         result = post_order(tree[node.left_node])
#     if node.right_node is not None:
#         result = post_order(tree[node.right_node])
#     result += node.data
#     return result

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

    




