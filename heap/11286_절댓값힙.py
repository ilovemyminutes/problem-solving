'''https://www.acmicpc.net/problem/11286
문제:
    '절댓값힙' := 다음의 두가지 연산을 지원하는 자료구조
        (1) 배열에 정수 x(x ≠ 0)를 push
        (2) 배열에서 절댓값이 가장 작은 값을 출력한 뒤 그 값을 배열에서 제거
            - 절댓값이 가장 작은 값이 여러 개일 경우 가장 작은 수를 출력한 뒤 그 값을 배열에서 제거한다.

입출력:
    - N: 연산 수 & N개 정수
        - 0: 배열 내 절댓값 가장 작은 원소 출력/제거(비어있을 경우 0 출력)
        - 그 외: push
'''
import sys
import heapq

ABS = 0
VALUE = 1

input = sys.stdin.readline

n = int(input())
operations = [int(input()) for _ in range(n)]

heap = []
for oper in operations:
    if oper == 0:
        if heap:
            popped = heapq.heappop(heap) # (ABS, VALUE)
            popped_array = [(popped[VALUE], popped[ABS])] # (VALUE, ABS)
            while heap:
                if heap[0][ABS] == popped[ABS]:
                    tmp = heapq.heappop(heap)
                    heapq.heappush(popped_array, (tmp[VALUE], tmp[ABS]))
                    continue
                break
            
            popped = heapq.heappop(popped_array) # (VALUE, ABS)
            for p in popped_array:
                heapq.heappush(heap, (p[1], p[0])) # (ABS, VALUE)
            print(popped[0]) # VALUE
        else:
            print(0)
                        
    else:
        heapq.heappush(heap, (abs(oper), oper))
            
