'''
문제: 주어진 tree 내 내부 node 개수 카운팅
internal node := 적어도 하나의 자식 노드를 가진 노드
'''
def count_internal_nodes(tree):
    is_internals = [False for _ in range(len(tree))]
    
    for parent_id in tree:
        if parent_id != -1 and is_internals[parent_id] is False:
            is_internals[parent_id] = True
        
    count = sum(is_internals)
    return count

tree = [1, 3, 1, -1, 3]
print(count_internal_nodes(tree)) # should print 2