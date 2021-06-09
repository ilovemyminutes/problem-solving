# 자료구조

## Queue

- FIFO(선입선출) 구조
- 선형 구조
- Enqueue: 큐 맨 뒤에 요소를 추가
- Dequeue: 큐 맨 앞쪽에 요소를 삭제
- Peek: front에 위치한 데이터를 읽음
- Front: 큐의 맨 앞의 위치(인덱스)
- Rear: 큐의 맨 뒤의 위치(인덱스)



## Tree

- 비선형 구조
- 단순히 값을 저장하는 용도보다는 효율적인 탐색 혹은 정렬을 위해 사용
- Node: 트리의 구성 요소
- Edge: 노드와 노드를 연결하는 선
- Root node: 트리 구조에서 최상위에 존재하는 노드
- Terminal node(=leaf node, 단말 노드): 밑으로 또 다른 노드가 존재하지 않는 마지막 노드
- Sub-tree: 어떠한 트리에 포함되는 트리
- Level: 트리의 각 층에 매기는 숫자
- Height: 트리 최고 레벨

#### 이진 트리(Binary tree)

- 각 노드가 최대 2개의 자식 노드를 가진 트리 구조
- 루트 노드를 중심으로 나뉘는 2개의 서브 트리가 이진 트리
- 서브 트리의 모든 서브 트리도 이진 트리
- 주어진 값 혹은 이보다 작거나 큰 값들을 평균 `O(logn)`의 시간 복잡도로 찾을 수 있음
- 이진 트리의 한 종류인 힙(`heap`)을 사용한 힙 정렬(`heap`)은 `O(nlogn)`의 시간복잡도를 가짐

##### 포화 이진 트리(Full binary tree): [?]

##### 완전 이진 트리(Complete binary tree): [?]

##### 이진 탐색 트리

- 이진 트리의 특수 케이스 중 하나
- 이진 트리 중 다음을 만족하는 트리는 이진 탐색 트리
  1. 모든 노드에 대해 왼쪽 자식 노드들의 값이 현재 노드 값보다 작음
  2. 오른쪽 자식 노드들의 값이 현재 노드의 값보다 큼
- 오른쪽으로는 큰 값만 주르륵, 왼쪽으로는 작은 값만 주르륵 들어가는 느낌([참고](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99AD154D5C5C50D932))
- 위의 룰이 설정되어 있으니, 원하는 값을 탐색할 때 저 룰을 바탕으로 빠르게 탐색할 수 있는 셈



## ETC

###### 선형구조

- 자료를 구성하고 있는 데이터들이 순차적으로 나열됨	
- 자료를 저장하고 꺼내는 것에 초점

##### 비선형 구조

- 데이터가 계층적 형태 또는 그래프 형태로 구성됨
- 표현에 초점



### References

- [자료구조: 큐(Queue) 이해하기](https://monsieursongsong.tistory.com/5)
- [위키피디아: 이진트리](https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%A7%84_%ED%8A%B8%EB%A6%AC)
- [파이썬을 이용해서 이진 탐색 트리 구현하기](https://geonlee.tistory.com/72)