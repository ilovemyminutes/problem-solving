'''n번째로 적게 팔린 책 찾기
sales의 각 원소: 해당 책의 id(인덱스)에 대한 단일 판매를 의미
- 책별 판매량은 unique를 가정
'''
from collections import Counter
import heapq

def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    counts = Counter(sales).items()
    heap = []
    for book_id, cnt in counts:
        heapq.heappush(heap, (cnt, book_id))
    
    for _ in range(n-1):
        heapq.heappop(heap)

    return heap[0][1]

if __name__ == "__main__":
    print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))