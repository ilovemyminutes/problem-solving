# Tips
## Algorithms

### Greedy

* 현재 상황에서 당장 좋은 것만 고르는 방법
* 문제를 풀기 위한 최소한의 아이디어를 떠올리는 능력이 핵심
* 정당성 분석 중요: *내가 만든 룰이 자동화된 상황에서 일반화될 수 있는가?*
* 일반적 상황에서 최적의 해를 보장할 수 없을 때가 많으나, 코테에서는 보장되는 상황을 전제
* DFS·BFS처럼 정해진 방법을 사용하기 보다, 자유롭게 방법을 도출하는 것이 중요

### DFS·BFS

#### DFS: 깊이 우선 탐색

* 루트 노드에서 분기마다 최대 깊이까지 탐색하는 방법
* 모든 노드를 방문할 떄 사용
* stack 자료 구조 사용(`list`)

```python
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def dfs(graph, start_node):
     visit = list()
     stack = list()

     stack.append(start_node)

     while stack:
         node = stack.pop()
         if node not in visit:
             visit.append(node)
             stack.extend(graph[node])

     return visit
```



#### BFS: 너비 우선 탐색

* 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법
* 두 노드 간 최단 경로 또는 임의 경로를 찾고 싶을 때 사용
* queue 자료 구조를 사용

```python
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def bfs(graph, start_node):
     visit = list()
     queue = list()

     queue.append(start_node) # 시작 노드 설정

     while queue: # queue에 더이상 담을 노드가 없을 떄까지, 즉, 모두 방문할 떄까지 루프 진행
         node = queue.pop(0) 
         if node not in visit: # 방문하지 않은 경우 방문 처리 & 
             visit.append(node)
             queue.extend(graph[node])

     return visit
```



### 정렬
* 오름차순이 기본값

#### 퀵정렬

* 가장 많이 활용되는 정렬 알고리즘
* '피벗을 잡아, 큰 데이터와 작은 데이터의 위치를 바꾼다'
    * 첫 번째 지점을 피벗으로 설정
    * 피벗이 아닌 가장 왼쪽 값에서 데이터를 오른쪽으로 필터링. 기준값보다 큰 값이 나올 때까지 계속 훑어
    * 가장 오른쪽 값에서 데이터를 왼쪽으로 필터링. 기준값보다 작은 값이 나올 때까지 계속 훑어
    * 왼쪽값과 오른쪽값이 교차했을 경우: 오른쪽값과 피벗값을 스왑
    * 왼쪽값과 오른쪽값이 교차하지 않는 경우: 왼쪽값과 오른쪽값을 스왑
```python
def quick_sort(array, start:'시작 index', end:'끝 index'):
    if start >= end:
        return
    pivot = start # 피벗
    left = start + 1 # 피벗의 바로 오른쪽 성분부터 훑는다
    right = end # 마지막 성분

    while left <= right:
        while left <= end and array[left] <= array[pivot]: # LEFT: 피벗값보다 큰 값이 발견될 떄까지 전진
            left += 1
        while right > start and array[right] >= array[pivot]: # RIGHT: 피벗값보다 작은 값이 발견될 떄까지 전진
            right -= 1
        if left > right: # LEFT, RIGHT가 교차했을 경우: 작은 데이터를 찾던 RIGHT <-> 피벗
            array[right], array[pivot] = array[pivot], array[right]
        else: # LEFT, RIGHT가 교차하지 않은 경우: LEFT <-> RIGHT
            array[left], array[right] = array[right], array[left]

    # 분할된 뒤, 분할별로 정렬이 진행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
```
#### 힙정렬

* 데이터를 **정렬된 상태**로 저장하기 위해 사용
* 힙 자료구조를 활용한 정렬 알고리즘, O(NlogN) <- 자료형이 따로 있는 것이 아님! 리스트 등을 힙의 자료 구조 방법으로 재배열하는 것
* 'N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업 <=> 정렬'
* 파이썬의 힙 자료구조는 '최소 힙' 기반으로 구현되어 있음
* Great Ref. https://www.daleseo.com/python-heapq/

```python
import heapq

# 힙 정렬 예시
# 파이썬의 힙은 최소 힙 기반
def heapsort(iterable):
    h = list()
    result = list()
    
    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value)
        
    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
        result.append(heapq.heappop(h))
    return result

# 리스트를 힙으로 변환하기
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap) # [1, 3, 5, 4, 8, 7]


# 최대 힙 구현
# heapq 모듕은 '최소 힙' 기반
# 원소가 튜플 형태인 경우, 첫번째 원소를 기준으로 정렬되는 것을 이용하여 약간의 트릭을 준다
import heapq
nums = [4, 1, 7, 3, 8, 5]
heap = []
for num in nums:
    heapq.heappush(heap, (-num, num))  # Trick: (우선 순위, 값) 

while heap:
    print(heapq.heappop(heap)[1])  # 8, 7, 5, ...
    
# k번째 최소/최대값
def smallest_k(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    min_k = None
    for _ in range(k):
        min_k = heapq.heappop(heap) # k번째로 작은 원소가 루트 노드가 될 때까지 pop 실행
    return min_k

print(smallest_k([4, 1, 7, 3, 8, 5], 3)) # 4
```

### 자료 구조

#### Stack
* 프링글스 통을 떠올리면 편함
* LIFO(Last In First Out): 가장 마지막 데이터가 가장 빨리 나간다.
* 파이썬의 list 자료형으로 구현 가능

#### Queue
* 양쪽 모두 뚫린 관을 떠올리면 편함
* FIFO(First in First Out): : 제일 먼저 입력된 데이터가 제일 먼저 나간다.
* 파이썬의 deque 모듈로 구현 가능

#### Priority Queue

* 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조. 데이터를 우선순위에 따라 처리하고 싶을 때 사용
* 스택은 가장 늦게 온 것이 먼저 나가고, 큐는 가장 먼저 온 것이 먼저 나가는 것처럼, 우선순위 큐는 가장 우선순위가 높은 것이 먼저 나감
* 리스트로 구현 - 삽입 O(1) / 삭제 O(N)
* 힙(Heap)으로 구현 - 삽입 O(logN) / 삭제 O(logN)
* N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업 <=> 정렬('힙 정렬'), O(NlogN)

#### etc
* 다중정렬 진행시, 뒷 정렬이 앞선 정렬의 순서를 망가뜨리지 않음
* Call by Reference / Call by Value
    * Call by Reference: 인자로 받은 변수의 **주소값**을 전달하는 방식
    * Call by Value: 변수를 **복사**한 값을 전달하는 방식
    * Python: Call by Object-reference(객체 속성에 따라 방식이 달라진다)
        * Immutable(`tuple`, `int`, `float`, `str` 등): Call by Value. 함수 내에서 global 변수를 수정할 수 없음
        * Mutable(`list`, `dict` , `set`등): Call by Reference. 함수 내에서 global 변수를 수정할 수 있음

## Functions
### collections
#### deque
* 큐 자료구조를 사용할 수있는 클래스
* .append(): 가장 우측에 데이터를 추가, O(1)
* .popleft(): 가장 좌측의 데이터를 제거 및 추출, O(1)
```python
from collections import deque
queue = deque()

queue.append(5) # 시간복잡도 O(1)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
```
#### Counter
* 원소별 빈도를 구할 떄 유용한 클래스
* dict의 하위 클래스, O(n)
```python
from collections import Counter

sample_list = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'e']
sample_str = 'aaaabbddccccccc'

>>> print(Counter(sample_list))
Counter({'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1})
>>> print(Counter(sample_str))
Counter({'a': 4, 'b': 2, 'd': 2, 'c': 7})
>>> counter = Counter(sample_str)
>>> print(counter.most_common(n=2))
[('a', 4), ('b',2)]
```
#### OrderedDict
* dict 자료형에 순서를 부여한 클래스, O(n)
* 순서를 활용하여 dict에 접근해야 할 때 유용
* .fromkeys(): iterable한 객체를 받아 각 원소를 키값으로 하는 OrderedDict 객체 생성
* .move_to_end(): 키값을 받아 해당 아이템을 맨 끝으로 이동
```python
from collections import OrderedDict
example = {'banana': 3, 'apple': 4, 'pear': 1, 'orange':2}

>>> od = OrderedDict(example)
>>> print(od)
OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])

od_sort = OrderedDict(sorted(example.items(), key=lambda x: x[-1]))
print(od_sort.keys(), od_sort.values())
>>> odict_keys(['pear', 'orange', 'banana', 'apple']) odict_values([1, 2, 3, 4])

# popitem(): 
>>> key, value = temp2.popitem()
>>> print('KEY:' key, 'VALUE:', value, 'OD:', temp2)
KEY: apple VALUE: 4 OD: OrderedDict([('pear', 1), ('orange', 2), ('banana', 3)])

>>> od = OrderedDict.fromkeys([1,2,3,])
>>> print(od)
OrderedDict([(1, None), (2, None), (3, None)])

>>> od = OrderedDict.fromkeys('abcd')
>>> print(od)
OrderedDict([('a', None), ('b', None), ('c', None), ('d', None)])

>>> od.move_to_end('b')
>>> print(from_keys)
OrderedDict([('a', None), ('c', None), ('d', None), ('b', None)])
```

### functools
#### reduce
* iterable한 객체에 반복적인 연산을 수행하여 하나의 값을 반환
```python
from functools import reduce
>>> print(reduce(sum, range(1, 11))) # 1부터 10까지의 합
55
```

#### cmp_to_key

* 커스텀 비교 규칙을 통한 정렬이 가능
* Reference. [python 내 마음대로 정렬(sort)!]([https://velog.io/@sparkbosing/python-%EB%82%B4-%EB%A7%88%EC%9D%8C%EB%8C%80%EB%A1%9C-%EC%A0%95%EB%A0%ACsort](https://velog.io/@sparkbosing/python-내-마음대로-정렬sort))
* 다음의 비교 함수를 바탕으로 정렬을 하는 것이 가능해짐

```python
def foo(x, y): # 2차원 벡터의 정렬을 진행할 때
    if x[0] == y[0]: # 앞 성분 값이 같으면
        return x[1] - y[1] # 뒷 성분 차를 기준으로 비교하겠다
    else: # 다르면
        return x[0] - y[0] # 앞 성분으로 비교하겠다
```

```python
from functools import cmp_to_key
arr = [(1,3), (1,2), (1,4)]
sorted(arr, key=cmp_to_key(foo)) # key 인자에 삽입하여 사용
```



### operator

#### mul
* 곱셈 연산
* redue 함수와 사용할 때 유용하다.
```python
import operator as op
>>> (reduce(op.mul, range(1,5))) # 1부터 4까지의 곱
24
```

## Attitude
* 한 방법에만 몰두하면 시야가 좁아진다. 때로는 큰 그림을 볼 것.
* 표준 라이브러리 유연하게 사용할 것
* '너무 무식하게 짰나?'라는 의심은 버리기
* 재귀 자꾸 쓰려고 해보자
    * 너무 재귀를 써야한다고 생각하지는 말자 