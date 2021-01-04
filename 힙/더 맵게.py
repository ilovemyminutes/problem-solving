'''https://programmers.co.kr/learn/courses/30/lessons/42626'''
import heapq

def solution(scoville, K):
    if _check(scoville, K):
        return 0
    
    heapq.heapify(scoville)
    cnt = 0
    possible = False
    while len(scoville) > 1:
        k1 = heapq.heappop(scoville)
        k2 = heapq.heappop(scoville)
        heapq.heappush(scoville, _mix(k1, k2))
        cnt += 1
        
        if _check(scoville, K):
            possible = True
            break
            
    return cnt if possible else -1
        
def _mix(k1, k2) -> int:
    return k1 + (k2 * 2)

def _check(scoville: list, K: int):
    return all(map(lambda x: x >= K, scoville))