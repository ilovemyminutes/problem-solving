'''
* 큐 자료구조
    * 먼저 삽입된 것이 먼저 나가는 자료구조
    * 양쪽이 모두 뚫린 터널을 생각하면 쉽다
'''
from collections import deque

queue = deque()

queue.append(5) # 시간복잡도 O(1)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)