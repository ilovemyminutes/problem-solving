# Binary Search
- 배열 내부 데이터가 정렬되어 있어야만 사용할 수 있은 알고리즘
- 탐색에 시작점, 끝점, 중간점의 3요소를 활용
- 정렬의 전제 하, 배열을 절반씩 나누어가면서 탐색하므로 시간복잡도는 `O(logN)`
(1) 주어진 배열의 시작점과 끝점 간 중간점을 찍음
(2) 중간점이 타깃 밸류와 일치할 경우 리턴, 그렇지 않을 경우 (3)으로
(3)
    - CASE1. 타깃 밸류가 중간점보다 작을 경우: 중간점의 바로 앞으로 끝점을 당겨옴(갱신)
    - CASE1. 타깃 밸류가 중간점보다 클 경우: 중간점의 바로 뒤로 시작점을 당겨옴(갱신)
(4) 타깃 밸류를 찾을 때까지 (1)-(3)을 반복(무한루프)
    - 시작점이 끝점보다 커질 경우 아무리 탐색해도 찾지 못한 것. 즉, 해당 배열에 타깃 밸류가 없음

- 구현
    (1) While문 활용
    ```python
        def binary_search(array, target, start, end):
            while start <= end:
                mid = (start + end) // 2

                # 딱 맞게 찾았을 경우
                if array[mid] == target:
                    return mid

                # 타깃값보다 중점값이 큰 경우: 끝점을 앞으로 당겨와
                elif array[mid] > target:
                    end = mid - 1

                # 타깃값보다 중점값이 작은 경우: 시작점을 뒤로 밀어
                else:
                    start = mid + 1

            return None # 없음
    ```
    (2) 재귀함수 활용
    ```python
        def binary_search(array, target, start, end):
            if start < end:
                return None
            mid = (start + end) // 2
            if array[mid] == target:
                return mid
            
            # 타깃값보다 중점값이 큰 경우: 끝점을 앞으로 당겨와
            elif array[mid] > target:
                return binary_search(array, target, start, mid-1) # NOTE. end <- mid-1
            
            # 타깃값보다 중점값이 작은 경우: 시작점을 뒤로 밀어
            else:
                return binary_search(array, target, mid+1, end) # NOTE. start <- mid+1
    ```
                