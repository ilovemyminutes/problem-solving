# Tips
## Algorithms
### 정렬
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
print(Counter(sample_list))
>>> Counter({'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1})
print(Counter(sample_str))
>>> Counter({'a': 4, 'b': 2, 'd': 2, 'c': 7})
```
#### OrderedDict
* dict 자료형에 순서를 부여한 클래스, O(n)
* 순서를 활용하여 dict에 접근해야 할 때 유용
* .fromkeys(): iterable한 객체를 받아 각 원소를 키값으로 하는 OrderedDict 객체 생성
* .move_to_end(): 키값을 받아 해당 아이템을 맨 끝으로 이동
```python
from collections import OrderedDict
example = {'banana': 3, 'apple': 4, 'pear': 1, 'orange':2}

od = OrderedDict(example)
print(od)
>>> OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])

od_sort = OrderedDict(sorted(example.items(), key=lambda x: x[-1]))
print(od_sort.keys(), od_sort.values())
>>> odict_keys(['pear', 'orange', 'banana', 'apple']) odict_values([1, 2, 3, 4])

# popitem(): 
key, value = temp2.popitem()
print('KEY:' key, 'VALUE:', value, 'OD:', temp2)
>>> KEY: apple VALUE: 4 OD: OrderedDict([('pear', 1), ('orange', 2), ('banana', 3)])

od = OrderedDict.fromkeys([1,2,3,])
print(od)
>>> OrderedDict([(1, None), (2, None), (3, None)])

od = OrderedDict.fromkeys('abcd')
print(od)
>>> OrderedDict([('a', None), ('b', None), ('c', None), ('d', None)])

od.move_to_end('b')
print(from_keys)
>>> OrderedDict([('a', None), ('c', None), ('d', None), ('b', None)])
```

## Attitude
* 한 방법에만 몰두하면 시야가 좁아진다. 때로는 뒤로 물러나서 큰 그림을 다시 볼 것.