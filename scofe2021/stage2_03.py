'''
단품, 세트, 패키지
단품의 조합 => 세트
단품은 단 하나의 세트에만 포함
세트는 또다른 세트에도 포함될 수 있음
패키지:
    - 세트와 단품으로 구성
    - 다른 세트에는 속하지 않음
*직접 관계되어 있지 않더라도 상/하위 관계 확인
6 6
6 4
6 5
4 1
4 2
4 3
1 4
4 1
6 5
1 6
6 3
4 3
'''
from collections import defaultdict
n, q = map(int, input().split()) # MAX: 500,000, MAX; N

relations = defaultdict(list)
for _ in range(n-1):
    sup, inf = map(int, input().split()) # always unique
    relations[sup].append(inf)

queries = []
for _ in range(q):
    sup, inf = map(int, input().split())
    queries.append((sup, inf))

def is_inferior(sup, inf, relations):
    inferiors = set(relations[sup])
    if inf in inferiors:
        print('yes')
        return
    current = relations[sup]
    visited = []
    while current:
        node = current.pop(0)
        inferiors.add(node)
        visited.append(node)

        current_inferiors = relations[node]
        if current_inferiors:
            for i in current_inferiors:
                if i not in visited:
                    current.append(i)
        if inf in inferiors:
            print('yes')
            return
    print('no')
    return

for query in queries:
    sup, inf = query[0], query[1]
    is_inferior(sup, inf, relations)

    


