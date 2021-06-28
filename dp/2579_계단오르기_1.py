"""계단 오르기 https://www.acmicpc.net/problem/2579
* 핵심: 2칸 전으로부터 왔느냐, 1칸 전으로부터 왔느냐
- 2칸 전: 2칸 전까지의 점수 + 현재 계단의 점수
- 1칸 전:
    - 1칸 전으로부터 왔다는 것은 이전에는 3칸 전의 위치였다는 것을 의미
    - 3칸 전까지의 점수 + 1칸 전 점수 + 현재 계단의 점수

* DP 구성: K번째 계단에 오르기까지의 최대 점수
dp = {
    1: 1번째 계단에 오르기까지의 최대 점수,
    2: 3번째 계단에 오르기까지의 최대 점수,
    ...
    N: N번째 계단에 오르기까지의 최대 점수
}

* 해결방법: K번째 최고 점수 구하기
    (1) 1칸 전에서 계단(k)로 올라온 경우: K번째 계단 점수 + (K-1)번째 계단 점수
        1칸 전에 올라왔으므로 이전에는 무조건 2칸 전에 올라옴
        => S(K) + S(K-1) + DP(K-3)
    (2) 2칸 전에서 계단(k)로 올라온 경우: K번째 계단 점수 + (K-2)번째 계단 점수
        => S(K) + DP(K-2)
    => (1),  (2) 중 더 큰 값을 선택하면 최대
"""
n = int(input())
scores = [0] + [int(input()) for _ in range(n)]

dp = dict()

def get_maximum(k):
    if k in dp:
        maximum = dp[k]

    elif k==0 or k == 1 or k == 2:
        maximum = sum(scores[:k+1])
        dp[k] = maximum

    elif k == 3:
        candidate1 = scores[1]+scores[3]
        candidate2 = scores[2]+scores[3]
        maximum = max(candidate1, candidate2)
        dp[k] = maximum

    else:
        candidate1 = scores[k] + scores[k-1] + get_maximum(k-3)
        candidate2 = scores[k] + get_maximum(k-2)
        maximum = max(candidate1, candidate2)
        dp[k] = maximum

    return maximum

print(get_maximum(n))


    
    
    

    
