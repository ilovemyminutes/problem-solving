from collections import deque

dp = list()
max_length = 0

def get_max_length(arr, i):
    global dp, max_length
    if dp[i] is None:
        que = deque(arr[i:])
        pre = None
        length = 0
        ascending = True
        while que:
            now = que.popleft()
            if pre is None:
                pre = now
                length += 1
                continue
                
            if ascending:
                if pre > now:
                    ascending = False
                length += 1
                pre = now
            else:
                if pre < now:
                    break
                length += 1
                pre = now
        # memoization
        for j in range(i, i+length):
            dp[j] = length
            if max_length < length:
                max_length = length
        return length
    
    elif dp[i] is not None:
        # check
        if 0 <= i+1 < len(arr) and dp[i+1] is None:
            que = deque(arr[i:])
            pre = None
            length = 0
            ascending = True
            while que:
                now = que.popleft()
                if pre is None:
                    pre = now
                    length += 1
                    continue
                    
                if ascending:
                    if pre > now:
                        ascending = False
                    length += 1
                    pre = now
                else:
                    if pre < now:
                        break
                    length += 1
                    pre = now
                    
            if length >= dp[i]:
                # memoization
                for j in range(i, i+length):
                    dp[j] = length
                    if max_length < length:
                        max_length = length
                return length
            else:
                return dp[i]
            
        # dp 리턴
        else:
            return dp[i]

def solution(arr: list) -> int:
    global dp, max_length
    dp = [None for _ in range(len(arr))]
    for idx in range(len(arr)):
        if (len(arr) - idx) < max_length:
            break
        get_max_length(arr=arr, i=idx)
    return max_length

if __name__ == '__main__':
    from time import time
    test = [7, 3, 4, 4, 8, 2, 5, 1]#*10000
    start = time()
    print(solution(test))
    print(time() - start)